'use client';

import { useState, useEffect, useCallback, useMemo } from 'react';
import {
  ExamDefinition,
  ExamMode,
  ExamAttempt,
  ExamLanguage,
  QuestionUserResponse,
} from '@/types/exam';
import {
  saveActiveSession,
  getActiveSession,
  clearActiveSession,
  saveCompletedAttempt,
  getLanguagePreference,
  setLanguagePreference,
} from '@/lib/storage/examStorage';
import { calculateExamScore, isAnswerCorrect } from '@/lib/scoreCalculator';
import { getLocalizedQuestion, getExamAvailableLanguages } from '@/lib/localization';

interface UseExamEngineProps {
  exam: ExamDefinition;
  mode: ExamMode;
  initialLanguage?: ExamLanguage;
  onFinishExam?: (attemptId: string) => void;
}

export function useExamEngine({ exam, mode, initialLanguage, onFinishExam }: UseExamEngineProps) {
  const [attemptId, setAttemptId] = useState<string>('');
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [responses, setResponses] = useState<Record<string, QuestionUserResponse>>({});
  const [timeRemainingSeconds, setTimeRemainingSeconds] = useState<number>(
    exam.timeLimitMinutes * 60
  );
  const [totalTimeSpentSeconds, setTotalTimeSpentSeconds] = useState<number>(0);
  const [isCompleted, setIsCompleted] = useState<boolean>(false);
  const [isInitialized, setIsInitialized] = useState<boolean>(false);

  // Idioma ativo do simulado
  const availableLanguages = useMemo(() => getExamAvailableLanguages(exam), [exam]);
  const [language, setLanguageState] = useState<ExamLanguage>(() => {
    if (initialLanguage && (initialLanguage === 'en' || initialLanguage === 'pt' || initialLanguage === 'es')) {
      return initialLanguage;
    }
    const pref = getLanguagePreference();
    return availableLanguages.includes(pref) ? pref : availableLanguages[0] || 'en';
  });

  const setLanguage = useCallback((newLang: ExamLanguage) => {
    setLanguageState(newLang);
    setLanguagePreference(newLang);
  }, []);

  // Modais de suporte e estado de pausa
  const [isQuestionMapOpen, setIsQuestionMapOpen] = useState<boolean>(false);
  const [isScratchpadOpen, setIsScratchpadOpen] = useState<boolean>(false);
  const [isReviewScreenOpen, setIsReviewScreenOpen] = useState<boolean>(false);
  const [isAbandonModalOpen, setIsAbandonModalOpen] = useState<boolean>(false);
  const [isPaused, setIsPaused] = useState<boolean>(false);
  const [isAbandoned, setIsAbandoned] = useState<boolean>(false);

  // Inicialização ou Retomada de Sessão
  useEffect(() => {
    const existing = getActiveSession(exam.id);

    if (existing && !existing.isCompleted && existing.mode === mode) {
      setAttemptId(existing.id);
      setCurrentIndex(existing.currentQuestionIndex || 0);
      setResponses(existing.responses || {});
      if (existing.language && (existing.language === 'en' || existing.language === 'pt' || existing.language === 'es')) {
        setLanguageState(existing.language);
      }
      const savedRemaining =
        typeof existing.timeRemainingSeconds === 'number'
          ? existing.timeRemainingSeconds
          : exam.timeLimitMinutes * 60;
      setTimeRemainingSeconds(savedRemaining);
      const savedSpent =
        typeof existing.totalTimeSpentSeconds === 'number'
          ? existing.totalTimeSpentSeconds
          : Math.max(0, exam.timeLimitMinutes * 60 - savedRemaining);
      setTotalTimeSpentSeconds(savedSpent);
      // Mantém pausado para que o usuário retome conscientemente sem perder tempo
      setIsPaused(true);
    } else {
      const newId = `attempt_${Date.now()}_${Math.random().toString(36).substring(2, 7)}`;
      setAttemptId(newId);
      setCurrentIndex(0);
      setResponses({});
      setTimeRemainingSeconds(exam.timeLimitMinutes * 60);
      setTotalTimeSpentSeconds(0);
      setIsPaused(false);
    }
    setIsInitialized(true);
  }, [exam.id, exam.timeLimitMinutes, mode]);

  // Questão Atual Localizada
  const rawQuestion = useMemo(() => {
    return exam.questions[currentIndex] || exam.questions[0];
  }, [exam.questions, currentIndex]);

  const currentQuestion = useMemo(() => {
    return getLocalizedQuestion(rawQuestion, language);
  }, [rawQuestion, language]);

  const currentResponse = useMemo(() => {
    if (!currentQuestion) return undefined;
    return responses[currentQuestion.id] || {
      questionId: currentQuestion.id,
      selectedOptionIds: [],
      struckOutOptionIds: [],
      isFlagged: false,
      timeSpentSeconds: 0,
    };
  }, [responses, currentQuestion]);

  // Função centralizada para salvar a sessão ativa
  const saveCurrentSession = useCallback(() => {
    if (!isInitialized || isCompleted || isAbandoned || !attemptId || !exam.id) return;

    const currentAttempt: ExamAttempt = {
      id: attemptId,
      examId: exam.id,
      examCode: exam.code,
      examTitle: exam.title,
      mode,
      language,
      startedAt: new Date(Date.now() - totalTimeSpentSeconds * 1000).toISOString(),
      timeRemainingSeconds,
      totalTimeSpentSeconds,
      isCompleted: false,
      currentQuestionIndex: currentIndex,
      responses,
    };

    saveActiveSession(currentAttempt);
  }, [
    isInitialized,
    isCompleted,
    isAbandoned,
    attemptId,
    exam.id,
    exam.code,
    exam.title,
    mode,
    language,
    totalTimeSpentSeconds,
    timeRemainingSeconds,
    currentIndex,
    responses,
  ]);

  // Auto-Save periódico a cada 5 segundos
  useEffect(() => {
    if (!isInitialized || isCompleted || isAbandoned || !attemptId) return;

    const interval = setInterval(() => {
      saveCurrentSession();
    }, 5000);

    return () => clearInterval(interval);
  }, [isInitialized, isCompleted, isAbandoned, attemptId, saveCurrentSession]);

  // Salva no beforeunload (ao fechar aba ou recarregar página)
  useEffect(() => {
    if (!isInitialized || isCompleted || isAbandoned || !attemptId) return;

    const handleBeforeUnload = () => {
      saveCurrentSession();
    };

    window.addEventListener('beforeunload', handleBeforeUnload);
    return () => window.removeEventListener('beforeunload', handleBeforeUnload);
  }, [isInitialized, isCompleted, attemptId, saveCurrentSession]);

  // Ações de Resposta
  const toggleOption = useCallback(
    (optionId: string) => {
      if (!currentQuestion || isCompleted) return;

      setResponses((prev) => {
        const qId = currentQuestion.id;
        const current = prev[qId] || {
          questionId: qId,
          selectedOptionIds: [],
          struckOutOptionIds: [],
          isFlagged: false,
          timeSpentSeconds: 0,
        };

        let newSelected: string[];
        const maxChoices =
          currentQuestion.type === 'single' ? 1 : currentQuestion.requiredChoices || 2;

        if (currentQuestion.type === 'single') {
          // Seleção única: seleciona a opção
          newSelected = [optionId];
        } else {
          // Múltipla seleção: adiciona ou remove respeitando o limite maxChoices
          if (current.selectedOptionIds.includes(optionId)) {
            newSelected = current.selectedOptionIds.filter((id) => id !== optionId);
          } else {
            if (current.selectedOptionIds.length >= maxChoices) {
              // Substitui a seleção mais antiga mantendo exatamente o limite de opções
              newSelected = [...current.selectedOptionIds.slice(1), optionId];
            } else {
              newSelected = [...current.selectedOptionIds, optionId];
            }
          }
        }

        // Se estava riscada, remove o risco ao selecionar
        const newStruck = (current.struckOutOptionIds || []).filter((id) => id !== optionId);
        const isCorrect = isAnswerCorrect(newSelected, currentQuestion.correctAnswers);

        return {
          ...prev,
          [qId]: {
            ...current,
            selectedOptionIds: newSelected,
            struckOutOptionIds: newStruck,
            isCorrect,
          },
        };
      });
    },
    [currentQuestion, isCompleted]
  );

  // Riscador de Alternativas (Strike-Through)
  const toggleStrikeThrough = useCallback(
    (optionId: string) => {
      if (!currentQuestion || isCompleted) return;

      setResponses((prev) => {
        const qId = currentQuestion.id;
        const current = prev[qId] || {
          questionId: qId,
          selectedOptionIds: [],
          struckOutOptionIds: [],
          isFlagged: false,
          timeSpentSeconds: 0,
        };

        const struck = current.struckOutOptionIds || [];
        const isCurrentlyStruck = struck.includes(optionId);
        const newStruck = isCurrentlyStruck
          ? struck.filter((id) => id !== optionId)
          : [...struck, optionId];

        // Se acabou de riscar a opção e ela estava selecionada, desmarca a seleção
        let newSelected = current.selectedOptionIds;
        if (!isCurrentlyStruck && newSelected.includes(optionId)) {
          newSelected = newSelected.filter((id) => id !== optionId);
        }

        const isCorrect = isAnswerCorrect(newSelected, currentQuestion.correctAnswers);

        return {
          ...prev,
          [qId]: {
            ...current,
            selectedOptionIds: newSelected,
            struckOutOptionIds: newStruck,
            isCorrect,
          },
        };
      });
    },
    [currentQuestion, isCompleted]
  );

  // Realce de Texto (Highlighting)
  const toggleHighlight = useCallback(
    (text: string) => {
      if (!currentQuestion || isCompleted || !text || text.trim().length === 0) return;
      const cleanText = text.trim();

      setResponses((prev) => {
        const qId = currentQuestion.id;
        const current = prev[qId] || {
          questionId: qId,
          selectedOptionIds: [],
          struckOutOptionIds: [],
          highlights: [],
          isFlagged: false,
          timeSpentSeconds: 0,
        };

        const existingHighlights = current.highlights || [];
        const isHighlighted = existingHighlights.includes(cleanText);
        const newHighlights = isHighlighted
          ? existingHighlights.filter((h) => h !== cleanText)
          : [...existingHighlights, cleanText];

        return {
          ...prev,
          [qId]: {
            ...current,
            highlights: newHighlights,
          },
        };
      });
    },
    [currentQuestion, isCompleted]
  );

  const clearHighlights = useCallback(() => {
    if (!currentQuestion || isCompleted) return;

    setResponses((prev) => {
      const qId = currentQuestion.id;
      const current = prev[qId] || {
        questionId: qId,
        selectedOptionIds: [],
        struckOutOptionIds: [],
        highlights: [],
        isFlagged: false,
        timeSpentSeconds: 0,
      };

      return {
        ...prev,
        [qId]: {
          ...current,
          highlights: [],
        },
      };
    });
  }, [currentQuestion, isCompleted]);

  // Verificar / Revelar Resposta no Modo Treino
  const toggleCheckAnswer = useCallback(() => {
    if (!currentQuestion || isCompleted) return;

    setResponses((prev) => {
      const qId = currentQuestion.id;
      const current = prev[qId] || {
        questionId: qId,
        selectedOptionIds: [],
        struckOutOptionIds: [],
        highlights: [],
        isFlagged: false,
        timeSpentSeconds: 0,
      };

      const currentlyChecked = !!current.isAnswerChecked;
      const isCorrect = isAnswerCorrect(
        current.selectedOptionIds,
        currentQuestion.correctAnswers
      );

      return {
        ...prev,
        [qId]: {
          ...current,
          isAnswerChecked: !currentlyChecked,
          isCorrect,
        },
      };
    });
  }, [currentQuestion, isCompleted]);

  // Marcar/Desmarcar Flag
  const toggleFlag = useCallback(() => {
    if (!currentQuestion || isCompleted) return;

    setResponses((prev) => {
      const qId = currentQuestion.id;
      const current = prev[qId] || {
        questionId: qId,
        selectedOptionIds: [],
        struckOutOptionIds: [],
        isFlagged: false,
        timeSpentSeconds: 0,
      };

      return {
        ...prev,
        [qId]: {
          ...current,
          isFlagged: !current.isFlagged,
        },
      };
    });
  }, [currentQuestion, isCompleted]);

  // Salvar Notas
  const setNotes = useCallback(
    (notes: string) => {
      if (!currentQuestion || isCompleted) return;

      setResponses((prev) => {
        const qId = currentQuestion.id;
        const current = prev[qId] || {
          questionId: qId,
          selectedOptionIds: [],
          struckOutOptionIds: [],
          isFlagged: false,
          timeSpentSeconds: 0,
        };

        return {
          ...prev,
          [qId]: {
            ...current,
            notes,
          },
        };
      });
    },
    [currentQuestion, isCompleted]
  );

  // Navegação
  const goToQuestion = useCallback(
    (index: number) => {
      if (index >= 0 && index < exam.questions.length) {
        setCurrentIndex(index);
        setIsQuestionMapOpen(false);
      }
    },
    [exam.questions.length]
  );

  const nextQuestion = useCallback(() => {
    if (currentIndex < exam.questions.length - 1) {
      setCurrentIndex((prev) => prev + 1);
    } else {
      // Se for a última questão no modo Real, abre a tela de revisão
      setIsReviewScreenOpen(true);
    }
  }, [currentIndex, exam.questions.length]);

  const prevQuestion = useCallback(() => {
    if (currentIndex > 0) {
      setCurrentIndex((prev) => prev - 1);
    }
  }, [currentIndex]);

  // Submissão do Exame
  const submitExam = useCallback(() => {
    if (isCompleted || !attemptId) return;

    const score = calculateExamScore(exam, responses);

    const finishedAttempt: ExamAttempt = {
      id: attemptId,
      examId: exam.id,
      examCode: exam.code,
      examTitle: exam.title,
      mode,
      language,
      startedAt: new Date(Date.now() - totalTimeSpentSeconds * 1000).toISOString(),
      completedAt: new Date().toISOString(),
      timeRemainingSeconds,
      totalTimeSpentSeconds,
      isCompleted: true,
      currentQuestionIndex: currentIndex,
      responses,
      score,
    };

    saveCompletedAttempt(finishedAttempt);
    clearActiveSession(exam.id);
    setIsCompleted(true);

    if (onFinishExam) {
      onFinishExam(attemptId);
    }
  }, [
    isCompleted,
    attemptId,
    exam,
    responses,
    mode,
    language,
    totalTimeSpentSeconds,
    timeRemainingSeconds,
    currentIndex,
    onFinishExam,
  ]);

  // Estatísticas de Progresso em Tempo Real
  const stats = useMemo(() => {
    const total = exam.questions.length;
    let answeredCount = 0;
    let flaggedCount = 0;

    exam.questions.forEach((q) => {
      const resp = responses[q.id];
      if (resp?.selectedOptionIds && resp.selectedOptionIds.length > 0) {
        answeredCount++;
      }
      if (resp?.isFlagged) {
        flaggedCount++;
      }
    });

    const unansweredCount = total - answeredCount;

    return {
      total,
      answeredCount,
      unansweredCount,
      flaggedCount,
      percentage: total > 0 ? Math.round((answeredCount / total) * 100) : 0,
    };
  }, [exam.questions, responses]);

  // Ações de Pausa e Abandono
  const pauseExam = useCallback(() => {
    if (isCompleted || isAbandoned) return;
    setIsPaused(true);
  }, [isCompleted, isAbandoned]);

  const resumeExam = useCallback(() => {
    setIsPaused(false);
  }, []);

  const togglePause = useCallback(() => {
    if (isCompleted || isAbandoned) return;
    setIsPaused((prev) => !prev);
  }, [isCompleted, isAbandoned]);

  const abandonExam = useCallback(() => {
    setIsAbandoned(true);
    setIsPaused(true);
    setIsAbandonModalOpen(false);
    clearActiveSession(exam.id);
  }, [exam.id]);

  // Suporte a Atalhos de Teclado
  useEffect(() => {
    if (
      !isInitialized ||
      isCompleted ||
      isAbandoned ||
      isReviewScreenOpen ||
      isScratchpadOpen ||
      isQuestionMapOpen ||
      isAbandonModalOpen
    ) {
      return;
    }

    const handleKeyDown = (e: KeyboardEvent) => {
      // Ignora se estiver digitando em input ou textarea
      const target = e.target as HTMLElement;
      if (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA') return;

      const key = e.key.toUpperCase();

      if (key === 'P') {
        e.preventDefault();
        togglePause();
        return;
      }

      // Se estiver pausado, não processa outros comandos do simulador
      if (isPaused) {
        if (key === 'ESCAPE' || key === 'ENTER') {
          e.preventDefault();
          resumeExam();
        }
        return;
      }

      if (['A', 'B', 'C', 'D', 'E', 'F', 'G'].includes(key) && currentQuestion) {
        const optionExists = currentQuestion.options.some((opt) => opt.id.toUpperCase() === key);
        if (optionExists) {
          e.preventDefault();
          toggleOption(key);
        }
      } else if (key === 'F') {
        // Se a tecla F for pressionada e não houver opção F, faz o flag
        const optionExists = currentQuestion?.options.some((opt) => opt.id.toUpperCase() === 'F');
        if (!optionExists) {
          e.preventDefault();
          toggleFlag();
        }
      } else if (key === 'ARROWLEFT') {
        e.preventDefault();
        prevQuestion();
      } else if (key === 'ARROWRIGHT' || key === 'ENTER') {
        e.preventDefault();
        nextQuestion();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [
    isInitialized,
    isCompleted,
    isAbandoned,
    isPaused,
    isReviewScreenOpen,
    isScratchpadOpen,
    isQuestionMapOpen,
    isAbandonModalOpen,
    currentQuestion,
    toggleOption,
    toggleFlag,
    prevQuestion,
    nextQuestion,
    togglePause,
    resumeExam,
  ]);

  // Timer countdown e contagem de tempo de estudo
  useEffect(() => {
    if (!isInitialized || isCompleted || isAbandoned || isPaused) {
      return;
    }

    const interval = setInterval(() => {
      if (mode === 'real') {
        setTimeRemainingSeconds((prev) => {
          if (prev <= 1) {
            clearInterval(interval);
            return 0;
          }
          return prev - 1;
        });
      }
      setTotalTimeSpentSeconds((prev) => prev + 1);
    }, 1000);

    return () => clearInterval(interval);
  }, [isInitialized, isCompleted, isAbandoned, isPaused, mode]);

  // Auto-submissão quando o tempo esgota no modo real
  useEffect(() => {
    if (isInitialized && !isCompleted && !isAbandoned && mode === 'real' && timeRemainingSeconds === 0) {
      submitExam();
    }
  }, [isInitialized, isCompleted, isAbandoned, mode, timeRemainingSeconds, submitExam]);

  // Formatação do tempo
  const formatTime = useCallback((secs: number) => {
    const hours = Math.floor(secs / 3600);
    const minutes = Math.floor((secs % 3600) / 60);
    const remainingSeconds = secs % 60;

    const pad = (n: number) => n.toString().padStart(2, '0');

    if (hours > 0) {
      return `${pad(hours)}:${pad(minutes)}:${pad(remainingSeconds)}`;
    }
    return `${pad(minutes)}:${pad(remainingSeconds)}`;
  }, []);

  const formattedTime = useMemo(
    () => formatTime(timeRemainingSeconds),
    [formatTime, timeRemainingSeconds]
  );
  const isTimerWarning = mode === 'real' && timeRemainingSeconds <= 900 && timeRemainingSeconds > 300; // <= 15 min
  const isTimerCritical = mode === 'real' && timeRemainingSeconds <= 300; // <= 5 min
  const isTimerRunning = !isPaused && !isAbandoned && mode === 'real' && isInitialized && !isCompleted;

  return {
    attemptId,
    currentIndex,
    currentQuestion,
    currentResponse,
    responses,
    stats,
    isCompleted,
    isInitialized,
    isAbandoned,
    timeRemainingSeconds,
    setTimeRemainingSeconds,
    totalTimeSpentSeconds,
    setTotalTimeSpentSeconds,
    // Idioma
    language,
    setLanguage,
    availableLanguages,
    // Timer e formatação
    formattedTime,
    isTimerWarning,
    isTimerCritical,
    isTimerRunning,
    // Pausa
    isPaused,
    setIsPaused,
    pauseExam,
    resumeExam,
    togglePause,
    saveCurrentSession,
    // Abandono
    abandonExam,
    // Modais
    isQuestionMapOpen,
    setIsQuestionMapOpen,
    isScratchpadOpen,
    setIsScratchpadOpen,
    isReviewScreenOpen,
    setIsReviewScreenOpen,
    isAbandonModalOpen,
    setIsAbandonModalOpen,
    // Ações
    toggleOption,
    toggleStrikeThrough,
    toggleHighlight,
    clearHighlights,
    toggleCheckAnswer,
    toggleFlag,
    setNotes,
    goToQuestion,
    nextQuestion,
    prevQuestion,
    submitExam,
  };
}
