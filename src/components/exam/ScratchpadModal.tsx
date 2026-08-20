'use client';

import React, { useState, useEffect } from 'react';
import { X, FileText, Check } from 'lucide-react';

interface ScratchpadModalProps {
  isOpen: boolean;
  onClose: () => void;
  questionNumber: number;
  initialNotes?: string;
  onSaveNotes: (notes: string) => void;
}

export function ScratchpadModal({
  isOpen,
  onClose,
  questionNumber,
  initialNotes = '',
  onSaveNotes,
}: ScratchpadModalProps) {
  const [notes, setNotes] = useState(initialNotes);

  useEffect(() => {
    setNotes(initialNotes);
  }, [initialNotes, isOpen]);

  if (!isOpen) return null;

  const handleSave = () => {
    onSaveNotes(notes);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-in fade-in duration-150">
      <div className="relative w-full max-w-lg rounded-2xl border border-slate-800 bg-slate-900 shadow-2xl overflow-hidden flex flex-col">
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <FileText className="h-5 w-5 text-amber-400" />
            <h2 className="text-base font-bold text-white">
              Notes for Question #{questionNumber}
            </h2>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6">
          <p className="text-xs text-slate-400 mb-3">
            Use this space as a scratchpad for your reasoning. Your notes are saved with this question.
          </p>
          <textarea
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            placeholder="e.g., Eliminate options C and D (not Multi-Region). Option A uses Aurora Global Database with RTO < 1m..."
            rows={6}
            className="w-full rounded-xl border border-slate-700 bg-slate-950 p-4 text-sm text-slate-100 placeholder-slate-500 focus:border-amber-400 focus:outline-none focus:ring-1 focus:ring-amber-400 resize-none font-mono"
            autoFocus
          />
        </div>

        {/* Footer */}
        <div className="px-6 py-3 border-t border-slate-800 bg-slate-950/40 flex justify-end gap-3">
          <button
            onClick={onClose}
            className="px-4 py-2 text-sm font-semibold rounded-lg text-slate-400 hover:text-white transition-colors"
          >
            Cancel
          </button>
          <button
            onClick={handleSave}
            className="flex items-center gap-1.5 px-4 py-2 text-sm font-semibold rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 transition-colors font-bold"
          >
            <Check className="h-4 w-4" />
            <span>Save Notes</span>
          </button>
        </div>
      </div>
    </div>
  );
}
