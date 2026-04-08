set shell := ["zsh", "-cu"]

# Run the full presentation deck with software decoding to avoid CUDA hwaccel probe warnings.
run:
	QT_FFMPEG_DECODING_HW_DEVICE_TYPES=none ./.venv/bin/manim-slides TitleSlide MigrationSlide MoERoutingSlide LengthBarrierSlide QualitySyncSlide ArchitectureSlide EnvironmentCoherenceSlide OptimizationComputeSlide EvaluationMetricsSlide SummarySlide ThanksSlide
