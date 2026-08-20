'use client';

import { useState, useEffect, useRef, useCallback } from 'react';

interface UseTimerProps {
  initialSeconds: number;
  countDown?: boolean;
  autoStart?: boolean;
  onTimeUp?: () => void;
}

export function useTimer({
  initialSeconds,
  countDown = true,
  autoStart = true,
  onTimeUp,
}: UseTimerProps) {
  const [seconds, setSeconds] = useState(initialSeconds);
  const [isRunning, setIsRunning] = useState(autoStart);
  const onTimeUpRef = useRef(onTimeUp);

  useEffect(() => {
    onTimeUpRef.current = onTimeUp;
  }, [onTimeUp]);

  useEffect(() => {
    setSeconds(initialSeconds);
  }, [initialSeconds]);

  useEffect(() => {
    if (!isRunning) return;

    const interval = setInterval(() => {
      setSeconds((prev) => {
        if (countDown) {
          if (prev <= 1) {
            clearInterval(interval);
            setIsRunning(false);
            if (onTimeUpRef.current) {
              onTimeUpRef.current();
            }
            return 0;
          }
          return prev - 1;
        } else {
          return prev + 1;
        }
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [isRunning, countDown]);

  const pause = useCallback(() => setIsRunning(false), []);
  const resume = useCallback(() => setIsRunning(true), []);
  const reset = useCallback(
    (newSeconds?: number) => {
      setSeconds(newSeconds !== undefined ? newSeconds : initialSeconds);
      setIsRunning(autoStart);
    },
    [initialSeconds, autoStart]
  );

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

  const isWarning = countDown && seconds <= 900 && seconds > 300; // <= 15 min
  const isCritical = countDown && seconds <= 300; // <= 5 min

  return {
    seconds,
    isRunning,
    formattedTime: formatTime(seconds),
    pause,
    resume,
    reset,
    isWarning,
    isCritical,
    setSeconds,
  };
}
