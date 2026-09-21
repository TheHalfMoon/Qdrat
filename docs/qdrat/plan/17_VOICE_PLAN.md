# Optional private voice

Owner: qdrat/voice. Himsat capture-session types and Wispral's separation of command/aside inform design; OpenWhispr and OpenSuperWhisper inform UX. Transcription engines are optional qualified adapters, initially whisper.cpp on supported CPU hardware; faster-whisper and sherpa-onnx are evaluated for hardware/language fit.

VoiceSession records initiator, participants/consent basis, source type, device permissions, capture start/stop, retention choice, model pack and artifact references. Audio capture, ASR, diarization, interpretation, TTS and action execution are separately cancellable. A microphone indicator is always visible. No background recording default and no mandatory remote service.

TranscriptSegment binds time offsets, language, confidence, speaker label and source digest. Speaker labels are uncertain observations, not proof of identity. Users can correct transcripts without destroying original provenance. Arabic dialects, English/Arabic code-switching, numbers, names, noisy rooms and silence require evaluation. Low-confidence speech produces a review prompt, not an executed command.

Dictation inserts text into a selected draft. Transcript-to-task/case/knowledge creates a preview with target, owner and extracted evidence. Voice commands use the same C01/C02/C06 authorization and confirmation as other actions. A quoted sentence, meeting aside or recognized name does not grant authority.

Raw audio retention defaults to shortest useful customer policy; transcript and derived summaries have separate explicit retention. Consent withdrawal/deletion respects legal hold and propagates to all derivatives and indexes. Participants can see recording state; imported recordings require declared lawful custody. Remote ASR requires an explicit profile and transfer approval.

Web/PWA supports foreground capture first. System-wide hotkeys and system audio require a later signed desktop adapter; macOS-only donor code cannot silently become a cross-platform promise. Offline model acquisition is via signed pack. No-AI/no-voice deployments carry no voice process.

Release evidence reports word/character error on consented synthetic/approved corpora, speaker attribution error, action-intent false positives, Arabic task completion, CPU/RAM/realtime factor and cancellation latency. Thresholds are set before the benchmark, not retrofitted to pass.
