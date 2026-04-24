set shell := ["zsh", "-cu"]

# Run the full presentation deck with software decoding to avoid CUDA hwaccel probe warnings.
run:
	QT_FFMPEG_DECODING_HW_DEVICE_TYPES=none ./.venv/bin/manim-slides TitleSlide MigrationSlide MoERoutingSlide LengthBarrierSlide QualitySyncSlide ArchitectureSlide EnvironmentCoherenceSlide OptimizationComputeSlide EvaluationMetricsSlide SummarySlide ThanksSlide

# Run Hyperon whitepaper deck with software decoding.
run-hyperon:
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/slide1_hyperon_intro.py HyperonWhitePaperTitleSlide
	QT_FFMPEG_DECODING_HW_DEVICE_TYPES=none ./.venv/bin/manim-slides present HyperonWhitePaperTitleSlide

# Run Hyperon Phase 1 foundations deck.
run-hyperon-phase1:
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/slide1_hyperon_intro.py HyperonWhitePaperTitleSlide
	for scene in Phase1QuestionOnlySlide Phase1StandardGraphGeneSlide Phase1BinaryEdgesNotEnoughSlide Phase1HypergraphSlide Phase1GraphLimitsAndFirstClassSlide Phase1MetagraphConceptSlide Phase1MetagraphGeneExampleSlide Phase1ContentAddressingSlide Phase1MerkleTreeSlide Phase1MerkleDagProgressiveSlide Phase1ImmutabilityVersioningSlide; do ./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/slide2_phase1_foundations.py "$scene"; done
	QT_FFMPEG_DECODING_HW_DEVICE_TYPES=none ./.venv/bin/manim-slides present HyperonWhitePaperTitleSlide Phase1QuestionOnlySlide Phase1StandardGraphGeneSlide Phase1BinaryEdgesNotEnoughSlide Phase1HypergraphSlide Phase1GraphLimitsAndFirstClassSlide Phase1MetagraphConceptSlide Phase1MetagraphGeneExampleSlide Phase1ContentAddressingSlide Phase1MerkleTreeSlide Phase1MerkleDagProgressiveSlide Phase1ImmutabilityVersioningSlide
