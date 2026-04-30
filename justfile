set shell := ["zsh", "-cu"]

hyperon_title_scene := "HyperonWhitePaperTitleSlide"
phase1_refined_scenes := "Phase1QuestionOnlySlide Phase1StandardGraphGeneSlide Phase1BinaryEdgesNotEnoughSlide Phase1HypergraphSlide Phase1GraphLimitsAndFirstClassSlide Phase1MetagraphConceptSlide Phase1MetagraphGeneExampleSlide Phase1ContentAddressingSlide Phase1MerkleTreeSlide Phase1MerkleDagProgressiveSlide Phase1ImmutabilityVersioningSlide Phase1TrieShapeSlide Phase1HierarchicalIndexingSlide Phase1PathBasedAddressingSlide Phase1LatticeHierarchySlide Phase1LatticeOperationsSlide Phase1QuantaleActionSlide Phase1QuantalePowersSlide Phase1ProbabilityVsLogicSlide Phase1SimpleTruthValueSlide Phase1PLNTruthMathSlide Phase1ExpectedTruthDecisionSlide Phase1ActiveInferenceLoopSlide Phase1PredictiveCodingMathSlide Phase1CausalCodingSimpsonSlide Phase1DoCalculusSurgerySlide Phase1BackdoorAdjustmentSlide"
atomspace_scenes := "AtomspaceSlide1 AtomspaceSlide2 AtomspaceSlide3 AtomspaceSlide4"
phase1_math_scenes := "Phase1SetsRelationsGraphs Phase1Hypergraphs Phase1MetagraphsCritical Phase1ContentAddressing Phase1MerkleStructures Phase1TriePathMap Phase1Quantales Phase1PLNTruthValues Phase1PredictiveCoding"
phase2_scenes := "Phase2AtomspaceSubstrate Phase2MORKEngine Phase2MeTTaLanguageStack Phase2SpaceAbstraction Phase2DistributedAtomspace Phase2StateManagement"
phase3_scenes := "Phase3TwoLoopDesign Phase3PLNReasoningEngine Phase3ECANAttentionSystem Phase3MOSESGeoEvo Phase3WILLIAMCompression Phase3PatternMiningBlending"
phase4_scenes := "Phase4WeaknessTheory Phase4GeodesicControl Phase4MetaMo Phase4SubRep Phase4TransWeave Phase4AlgorithmicChemistry Phase4SchrodingerBridge"
phase5_scenes := "Phase5IntegrationProblem Phase5OutsideMode Phase5QuantiMORK Phase5PCNoBprop Phase5SelectiveRefinementWILLIAM"
phase6_scenes := "Phase6WhySelfModification Phase6InvariantHierarchies Phase6StabilityTypes Phase6SafePipeline Phase6GovernanceASIChain Phase6AuditableCognition Phase6TheoremProvingBenchmark"
phase789_scenes := "Phase7Applications Phase7QwestorDetail Phase7MinecraftBioMath Phase8MasterPlan Phase8Workstreams Phase9FullSystemView Phase9CoreUnifyingIdeas HyperClawOrchestrationLayer HyperClawArchitecturePillars HyperClawAttentionLoops HyperClawUseCasesAndEvolution HyperClawQuoteBridge FinalConclusion"

# Run the full presentation deck with software decoding to avoid CUDA hwaccel probe warnings.
run:
	QT_FFMPEG_DECODING_HW_DEVICE_TYPES=none ./.venv/bin/manim-slides TitleSlide MigrationSlide MoERoutingSlide LengthBarrierSlide QualitySyncSlide ArchitectureSlide EnvironmentCoherenceSlide OptimizationComputeSlide EvaluationMetricsSlide SummarySlide ThanksSlide

# Run Hyperon whitepaper deck with software decoding.
run-hyperon:
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/slide1_hyperon_intro.py HyperonWhitePaperTitleSlide
	QT_FFMPEG_DECODING_HW_DEVICE_TYPES=none ./.venv/bin/manim-slides present HyperonWhitePaperTitleSlide

# Run Hyperon Phase 1 foundations deck + Atomspace slides.
run-hyperon-phase1:
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/slide1_hyperon_intro.py HyperonWhitePaperTitleSlide
	for scene in Phase1QuestionOnlySlide Phase1StandardGraphGeneSlide Phase1BinaryEdgesNotEnoughSlide Phase1HypergraphSlide Phase1GraphLimitsAndFirstClassSlide Phase1MetagraphConceptSlide Phase1MetagraphGeneExampleSlide Phase1ContentAddressingSlide Phase1MerkleTreeSlide Phase1MerkleDagProgressiveSlide Phase1ImmutabilityVersioningSlide Phase1TrieShapeSlide Phase1HierarchicalIndexingSlide Phase1PathBasedAddressingSlide Phase1LatticeHierarchySlide Phase1LatticeOperationsSlide Phase1QuantaleActionSlide Phase1QuantalePowersSlide Phase1ProbabilityVsLogicSlide Phase1SimpleTruthValueSlide Phase1PLNTruthMathSlide Phase1ExpectedTruthDecisionSlide Phase1ActiveInferenceLoopSlide Phase1PredictiveCodingMathSlide Phase1CausalCodingSimpsonSlide Phase1DoCalculusSurgerySlide Phase1BackdoorAdjustmentSlide; do ./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/slide2_phase1_foundations.py "$scene"; done
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/slide3_atomspace.py AtomspaceSlide1 AtomspaceSlide2 AtomspaceSlide3 AtomspaceSlide4
	QT_FFMPEG_DECODING_HW_DEVICE_TYPES=none ./.venv/bin/manim-slides present HyperonWhitePaperTitleSlide Phase1QuestionOnlySlide Phase1StandardGraphGeneSlide Phase1BinaryEdgesNotEnoughSlide Phase1HypergraphSlide Phase1GraphLimitsAndFirstClassSlide Phase1MetagraphConceptSlide Phase1MetagraphGeneExampleSlide Phase1ContentAddressingSlide Phase1MerkleTreeSlide Phase1MerkleDagProgressiveSlide Phase1ImmutabilityVersioningSlide Phase1TrieShapeSlide Phase1HierarchicalIndexingSlide Phase1PathBasedAddressingSlide Phase1LatticeHierarchySlide Phase1LatticeOperationsSlide Phase1QuantaleActionSlide Phase1QuantalePowersSlide Phase1ProbabilityVsLogicSlide Phase1SimpleTruthValueSlide Phase1PLNTruthMathSlide Phase1ExpectedTruthDecisionSlide Phase1ActiveInferenceLoopSlide Phase1PredictiveCodingMathSlide Phase1CausalCodingSimpsonSlide Phase1DoCalculusSurgerySlide Phase1BackdoorAdjustmentSlide AtomspaceSlide1 AtomspaceSlide2 AtomspaceSlide3 AtomspaceSlide4

# Run the new Atomspace presentation (4 slides).
run-atomspace:
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/slide3_atomspace.py AtomspaceSlide1 AtomspaceSlide2 AtomspaceSlide3 AtomspaceSlide4
	QT_FFMPEG_DECODING_HW_DEVICE_TYPES=none ./.venv/bin/manim-slides present AtomspaceSlide1 AtomspaceSlide2 AtomspaceSlide3 AtomspaceSlide4

# Run full Hyperon presentation: intro, phase 1 foundations, Atomspace, and phases 1-9.
run-all:
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/slide1_hyperon_intro.py {{hyperon_title_scene}}
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/slide2_phase1_foundations.py {{phase1_refined_scenes}}
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/phase2_core_infrastructure.py {{phase2_scenes}}
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/phase3_primus_cognitive.py {{phase3_scenes}}
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/slide3_atomspace.py {{atomspace_scenes}}
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/phase4_advanced_primus.py {{phase4_scenes}}
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/phase5_neural_symbolic.py {{phase5_scenes}}
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/phase6_self_modification_asi.py {{phase6_scenes}}
	./.venv/bin/manim-slides render -ql ./hyperon_whitepaper_slides/phase7_8_9_applications_roadmap_synthesis.py {{phase789_scenes}}
	QT_FFMPEG_DECODING_HW_DEVICE_TYPES=none ./.venv/bin/manim-slides present {{hyperon_title_scene}} {{phase1_refined_scenes}} {{phase2_scenes}} {{phase3_scenes}} {{atomspace_scenes}} {{phase4_scenes}} {{phase5_scenes}} {{phase6_scenes}} {{phase789_scenes}}
