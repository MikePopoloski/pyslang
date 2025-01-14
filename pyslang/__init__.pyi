"""
Python bindings for slang, the SystemVerilog compiler library
"""
from __future__ import annotations

import os
import typing

import pybind11_stubgen.typing_ext

__all__ = ['ASTContext', 'ASTFlags', 'AbortAssertionExpr', 'AcceptOnPropertyExprSyntax', 'ActionBlockSyntax', 'AnonymousProgramSymbol', 'AnonymousProgramSyntax', 'AnsiPortListSyntax', 'AnsiUdpPortListSyntax', 'ArbitrarySymbolExpression', 'ArgumentDirection', 'ArgumentListSyntax', 'ArgumentSyntax', 'ArrayOrRandomizeMethodExpressionSyntax', 'AssertionExpr', 'AssertionExprKind', 'AssertionInstanceExpression', 'AssertionItemPortListSyntax', 'AssertionItemPortSyntax', 'AssertionKind', 'AssertionPortSymbol', 'AssignmentExpression', 'AssignmentPatternExpressionBase', 'AssignmentPatternExpressionSyntax', 'AssignmentPatternItemSyntax', 'AssignmentPatternSyntax', 'AssociativeArrayType', 'AttributeInstanceSyntax', 'AttributeSpecSyntax', 'AttributeSymbol', 'BadExpressionSyntax', 'Bag', 'BeginKeywordsDirectiveSyntax', 'BinSelectWithFilterExpr', 'BinSelectWithFilterExprSyntax', 'BinaryAssertionExpr', 'BinaryAssertionOperator', 'BinaryBinsSelectExpr', 'BinaryBinsSelectExprSyntax', 'BinaryBlockEventExpressionSyntax', 'BinaryConditionalDirectiveExpressionSyntax', 'BinaryEventExpressionSyntax', 'BinaryExpression', 'BinaryExpressionSyntax', 'BinaryOperator', 'BinaryPropertyExprSyntax', 'BinarySequenceExprSyntax', 'BindDirectiveSyntax', 'BindTargetListSyntax', 'BinsSelectConditionExprSyntax', 'BinsSelectExpr', 'BinsSelectExprKind', 'BinsSelectExpressionSyntax', 'BinsSelectionSyntax', 'BitSelectSyntax', 'BlockCoverageEventSyntax', 'BlockEventExpressionSyntax', 'BlockEventListControl', 'BlockStatement', 'BlockStatementSyntax', 'BreakStatement', 'BufferID', 'BumpAllocator', 'CHandleType', 'CallExpression', 'CaseAssertionExpr', 'CaseGenerateSyntax', 'CaseItemSyntax', 'CasePropertyExprSyntax', 'CaseStatement', 'CaseStatementCondition', 'CaseStatementSyntax', 'CastExpressionSyntax', 'CellConfigRuleSyntax', 'ChargeStrengthSyntax', 'CheckerDataDeclarationSyntax', 'CheckerDeclarationSyntax', 'CheckerInstanceBodySymbol', 'CheckerInstanceStatementSyntax', 'CheckerInstanceSymbol', 'CheckerInstantiationSyntax', 'CheckerSymbol', 'ClassDeclarationSyntax', 'ClassMethodDeclarationSyntax', 'ClassMethodPrototypeSyntax', 'ClassNameSyntax', 'ClassPropertyDeclarationSyntax', 'ClassPropertySymbol', 'ClassSpecifierSyntax', 'ClassType', 'ClockVarSymbol', 'ClockingAssertionExpr', 'ClockingBlockSymbol', 'ClockingDeclarationSyntax', 'ClockingDirectionSyntax', 'ClockingEventExpression', 'ClockingItemSyntax', 'ClockingPropertyExprSyntax', 'ClockingSequenceExprSyntax', 'ClockingSkew', 'ClockingSkewSyntax', 'ColonExpressionClauseSyntax', 'CommandLineOptions', 'Compilation', 'CompilationFlags', 'CompilationOptions', 'CompilationUnitSymbol', 'CompilationUnitSyntax', 'ConcatenationExpression', 'ConcatenationExpressionSyntax', 'ConcurrentAssertionMemberSyntax', 'ConcurrentAssertionStatement', 'ConcurrentAssertionStatementSyntax', 'ConditionBinsSelectExpr', 'ConditionalAssertionExpr', 'ConditionalBranchDirectiveSyntax', 'ConditionalConstraint', 'ConditionalConstraintSyntax', 'ConditionalDirectiveExpressionSyntax', 'ConditionalExpression', 'ConditionalExpressionSyntax', 'ConditionalPathDeclarationSyntax', 'ConditionalPatternSyntax', 'ConditionalPredicateSyntax', 'ConditionalPropertyExprSyntax', 'ConditionalStatement', 'ConditionalStatementSyntax', 'ConfigBlockSymbol', 'ConfigCellIdentifierSyntax', 'ConfigDeclarationSyntax', 'ConfigInstanceIdentifierSyntax', 'ConfigLiblistSyntax', 'ConfigRuleClauseSyntax', 'ConfigRuleSyntax', 'ConfigUseClauseSyntax', 'ConstantPattern', 'ConstantRange', 'ConstantValue', 'Constraint', 'ConstraintBlockFlags', 'ConstraintBlockSymbol', 'ConstraintBlockSyntax', 'ConstraintDeclarationSyntax', 'ConstraintItemSyntax', 'ConstraintKind', 'ConstraintList', 'ConstraintPrototypeSyntax', 'ContinueStatement', 'ContinuousAssignSymbol', 'ContinuousAssignSyntax', 'ConversionExpression', 'ConversionKind', 'CopyClassExpression', 'CopyClassExpressionSyntax', 'CoverCrossBodySymbol', 'CoverCrossSymbol', 'CoverCrossSyntax', 'CoverageBinInitializerSyntax', 'CoverageBinSymbol', 'CoverageBinsArraySizeSyntax', 'CoverageBinsSyntax', 'CoverageIffClauseSyntax', 'CoverageOptionSetter', 'CoverageOptionSyntax', 'CovergroupBodySymbol', 'CovergroupDeclarationSyntax', 'CovergroupType', 'CoverpointSymbol', 'CoverpointSyntax', 'CrossIdBinsSelectExpr', 'CycleDelayControl', 'DPIExportSyntax', 'DPIImportSyntax', 'DPIOpenArrayType', 'DataDeclarationSyntax', 'DataTypeExpression', 'DataTypeSyntax', 'DeclaratorSyntax', 'DeclaredType', 'DefParamAssignmentSyntax', 'DefParamSymbol', 'DefParamSyntax', 'DefaultCaseItemSyntax', 'DefaultClockingReferenceSyntax', 'DefaultConfigRuleSyntax', 'DefaultCoverageBinInitializerSyntax', 'DefaultDecayTimeDirectiveSyntax', 'DefaultDisableDeclarationSyntax', 'DefaultDistItemSyntax', 'DefaultExtendsClauseArgSyntax', 'DefaultFunctionPortSyntax', 'DefaultNetTypeDirectiveSyntax', 'DefaultPropertyCaseItemSyntax', 'DefaultRsCaseItemSyntax', 'DefaultSkewItemSyntax', 'DefaultTriregStrengthDirectiveSyntax', 'DeferredAssertionSyntax', 'DefineDirectiveSyntax', 'DefinitionKind', 'DefinitionSymbol', 'Delay3Control', 'Delay3Syntax', 'DelayControl', 'DelaySyntax', 'DelayedSequenceElementSyntax', 'DelayedSequenceExprSyntax', 'DiagCode', 'DiagGroup', 'DiagSubsystem', 'Diagnostic', 'DiagnosticClient', 'DiagnosticEngine', 'DiagnosticSeverity', 'Diagnostics', 'Diags', 'DimensionKind', 'DimensionSpecifierSyntax', 'DirectiveSyntax', 'DisableConstraintSyntax', 'DisableForkStatement', 'DisableForkStatementSyntax', 'DisableIffAssertionExpr', 'DisableIffSyntax', 'DisableSoftConstraint', 'DisableStatement', 'DisableStatementSyntax', 'DistConstraintListSyntax', 'DistExpression', 'DistItemBaseSyntax', 'DistItemSyntax', 'DistWeightSyntax', 'DividerClauseSyntax', 'DoWhileLoopStatement', 'DoWhileStatementSyntax', 'DotMemberClauseSyntax', 'DriveStrengthSyntax', 'Driver', 'DriverKind', 'DynamicArrayType', 'EdgeControlSpecifierSyntax', 'EdgeDescriptorSyntax', 'EdgeKind', 'EdgeSensitivePathSuffixSyntax', 'ElabSystemTaskKind', 'ElabSystemTaskSymbol', 'ElabSystemTaskSyntax', 'ElementSelectExpression', 'ElementSelectExpressionSyntax', 'ElementSelectSyntax', 'ElseClauseSyntax', 'ElseConstraintClauseSyntax', 'ElsePropertyClauseSyntax', 'EmptyArgumentExpression', 'EmptyArgumentSyntax', 'EmptyIdentifierNameSyntax', 'EmptyMemberSymbol', 'EmptyMemberSyntax', 'EmptyNonAnsiPortSyntax', 'EmptyPortConnectionSyntax', 'EmptyQueueExpressionSyntax', 'EmptyStatement', 'EmptyStatementSyntax', 'EmptyTimingCheckArgSyntax', 'EnumType', 'EnumTypeSyntax', 'EnumValueSymbol', 'EqualsAssertionArgClauseSyntax', 'EqualsTypeClauseSyntax', 'EqualsValueClauseSyntax', 'ErrorType', 'EvalContext', 'EvalFlags', 'EvaluatedDimension', 'EventControlSyntax', 'EventControlWithExpressionSyntax', 'EventExpressionSyntax', 'EventListControl', 'EventTriggerStatement', 'EventTriggerStatementSyntax', 'EventType', 'ExplicitAnsiPortSyntax', 'ExplicitImportSymbol', 'ExplicitNonAnsiPortSyntax', 'Expression', 'ExpressionConstraint', 'ExpressionConstraintSyntax', 'ExpressionCoverageBinInitializerSyntax', 'ExpressionKind', 'ExpressionOrDistSyntax', 'ExpressionPatternSyntax', 'ExpressionStatement', 'ExpressionStatementSyntax', 'ExpressionSyntax', 'ExpressionTimingCheckArgSyntax', 'ExtendsClauseSyntax', 'ExternInterfaceMethodSyntax', 'ExternModuleDeclSyntax', 'ExternUdpDeclSyntax', 'FieldSymbol', 'FilePathSpecSyntax', 'FirstMatchAssertionExpr', 'FirstMatchSequenceExprSyntax', 'FixedSizeUnpackedArrayType', 'FloatingType', 'ForLoopStatement', 'ForLoopStatementSyntax', 'ForVariableDeclarationSyntax', 'ForeachConstraint', 'ForeachLoopListSyntax', 'ForeachLoopStatement', 'ForeachLoopStatementSyntax', 'ForeverLoopStatement', 'ForeverStatementSyntax', 'FormalArgumentSymbol', 'ForwardTypeRestriction', 'ForwardTypeRestrictionSyntax', 'ForwardTypedefDeclarationSyntax', 'ForwardingTypedefSymbol', 'FunctionDeclarationSyntax', 'FunctionPortBaseSyntax', 'FunctionPortListSyntax', 'FunctionPortSyntax', 'FunctionPrototypeSyntax', 'GenerateBlockArraySymbol', 'GenerateBlockSymbol', 'GenerateBlockSyntax', 'GenerateRegionSyntax', 'GenericClassDefSymbol', 'GenvarDeclarationSyntax', 'GenvarSymbol', 'HierarchicalInstanceSyntax', 'HierarchicalValueExpression', 'HierarchyInstantiationSyntax', 'IdWithExprCoverageBinInitializerSyntax', 'IdentifierNameSyntax', 'IdentifierSelectNameSyntax', 'IfGenerateSyntax', 'IfNonePathDeclarationSyntax', 'IffEventClauseSyntax', 'ImmediateAssertionMemberSyntax', 'ImmediateAssertionStatement', 'ImmediateAssertionStatementSyntax', 'ImplementsClauseSyntax', 'ImplicationConstraint', 'ImplicationConstraintSyntax', 'ImplicitAnsiPortSyntax', 'ImplicitEventControl', 'ImplicitEventControlSyntax', 'ImplicitNonAnsiPortSyntax', 'ImplicitTypeSyntax', 'IncludeDirectiveSyntax', 'InsideExpression', 'InsideExpressionSyntax', 'InstanceArraySymbol', 'InstanceBodySymbol', 'InstanceConfigRuleSyntax', 'InstanceNameSyntax', 'InstanceSymbol', 'InstanceSymbolBase', 'IntegerLiteral', 'IntegerTypeSyntax', 'IntegerVectorExpressionSyntax', 'IntegralFlags', 'IntegralType', 'InterfacePortHeaderSyntax', 'InterfacePortSymbol', 'IntersectClauseSyntax', 'InvalidAssertionExpr', 'InvalidBinsSelectExpr', 'InvalidConstraint', 'InvalidExpression', 'InvalidPattern', 'InvalidStatement', 'InvalidTimingControl', 'InvocationExpressionSyntax', 'IteratorSymbol', 'JumpStatementSyntax', 'KeywordNameSyntax', 'KeywordTypeSyntax', 'LValue', 'LValueReferenceExpression', 'LanguageVersion', 'LetDeclSymbol', 'LetDeclarationSyntax', 'LexerOptions', 'LibraryDeclarationSyntax', 'LibraryIncDirClauseSyntax', 'LibraryIncludeStatementSyntax', 'LibraryMapSyntax', 'LineDirectiveSyntax', 'LiteralBase', 'LiteralExpressionSyntax', 'LocalAssertionVarSymbol', 'LocalVariableDeclarationSyntax', 'Lookup', 'LookupFlags', 'LookupLocation', 'LookupResult', 'LookupResultFlags', 'LoopConstraintSyntax', 'LoopGenerateSyntax', 'LoopStatementSyntax', 'MacroActualArgumentListSyntax', 'MacroActualArgumentSyntax', 'MacroArgumentDefaultSyntax', 'MacroFormalArgumentListSyntax', 'MacroFormalArgumentSyntax', 'MacroUsageSyntax', 'MatchesClauseSyntax', 'MemberAccessExpression', 'MemberAccessExpressionSyntax', 'MemberSyntax', 'MethodFlags', 'MethodPrototypeSymbol', 'MinTypMax', 'MinTypMaxExpression', 'MinTypMaxExpressionSyntax', 'ModportClockingPortSyntax', 'ModportClockingSymbol', 'ModportDeclarationSyntax', 'ModportExplicitPortSyntax', 'ModportItemSyntax', 'ModportNamedPortSyntax', 'ModportPortSymbol', 'ModportPortSyntax', 'ModportSimplePortListSyntax', 'ModportSubroutinePortListSyntax', 'ModportSubroutinePortSyntax', 'ModportSymbol', 'ModuleDeclarationSyntax', 'ModuleHeaderSyntax', 'MultiPortSymbol', 'MultipleConcatenationExpressionSyntax', 'NameSyntax', 'NameValuePragmaExpressionSyntax', 'NamedArgumentSyntax', 'NamedBlockClauseSyntax', 'NamedConditionalDirectiveExpressionSyntax', 'NamedLabelSyntax', 'NamedParamAssignmentSyntax', 'NamedPortConnectionSyntax', 'NamedStructurePatternMemberSyntax', 'NamedTypeSyntax', 'NamedValueExpression', 'NetAliasSymbol', 'NetAliasSyntax', 'NetDeclarationSyntax', 'NetPortHeaderSyntax', 'NetStrengthSyntax', 'NetSymbol', 'NetType', 'NetTypeDeclarationSyntax', 'NewArrayExpression', 'NewArrayExpressionSyntax', 'NewClassExpression', 'NewClassExpressionSyntax', 'NewCovergroupExpression', 'NonAnsiPortListSyntax', 'NonAnsiPortSyntax', 'NonAnsiUdpPortListSyntax', 'NonConstantFunction', 'Null', 'NullLiteral', 'NullType', 'NumberPragmaExpressionSyntax', 'OneStepDelayControl', 'OneStepDelaySyntax', 'OrderedArgumentSyntax', 'OrderedParamAssignmentSyntax', 'OrderedPortConnectionSyntax', 'OrderedStructurePatternMemberSyntax', 'PackageExportAllDeclarationSyntax', 'PackageExportDeclarationSyntax', 'PackageImportDeclarationSyntax', 'PackageImportItemSyntax', 'PackageSymbol', 'PackedArrayType', 'PackedStructType', 'PackedUnionType', 'ParamAssignmentSyntax', 'ParameterDeclarationBaseSyntax', 'ParameterDeclarationStatementSyntax', 'ParameterDeclarationSyntax', 'ParameterPortListSyntax', 'ParameterSymbol', 'ParameterSymbolBase', 'ParameterValueAssignmentSyntax', 'ParenExpressionListSyntax', 'ParenPragmaExpressionSyntax', 'ParenthesizedBinsSelectExprSyntax', 'ParenthesizedConditionalDirectiveExpressionSyntax', 'ParenthesizedEventExpressionSyntax', 'ParenthesizedExpressionSyntax', 'ParenthesizedPatternSyntax', 'ParenthesizedPropertyExprSyntax', 'ParenthesizedSequenceExprSyntax', 'ParserOptions', 'PathDeclarationSyntax', 'PathDescriptionSyntax', 'PathSuffixSyntax', 'Pattern', 'PatternCaseItemSyntax', 'PatternCaseStatement', 'PatternKind', 'PatternSyntax', 'PatternVarSymbol', 'PortConcatenationSyntax', 'PortConnection', 'PortConnectionSyntax', 'PortDeclarationSyntax', 'PortExpressionSyntax', 'PortHeaderSyntax', 'PortListSyntax', 'PortReferenceSyntax', 'PortSymbol', 'PostfixUnaryExpressionSyntax', 'PragmaDirectiveSyntax', 'PragmaExpressionSyntax', 'PredefinedIntegerType', 'PrefixUnaryExpressionSyntax', 'PreprocessorOptions', 'PrimaryBlockEventExpressionSyntax', 'PrimaryExpressionSyntax', 'PrimitiveInstanceSymbol', 'PrimitiveInstantiationSyntax', 'PrimitivePortDirection', 'PrimitivePortSymbol', 'PrimitiveSymbol', 'ProceduralAssignStatement', 'ProceduralAssignStatementSyntax', 'ProceduralBlockKind', 'ProceduralBlockSymbol', 'ProceduralBlockSyntax', 'ProceduralCheckerStatement', 'ProceduralDeassignStatement', 'ProceduralDeassignStatementSyntax', 'ProductionSyntax', 'PropertyCaseItemSyntax', 'PropertyDeclarationSyntax', 'PropertyExprSyntax', 'PropertySpecSyntax', 'PropertySymbol', 'PropertyType', 'PullStrengthSyntax', 'PulseStyleDeclarationSyntax', 'PulseStyleKind', 'PulseStyleSymbol', 'QueueDimensionSpecifierSyntax', 'QueueType', 'RandCaseItemSyntax', 'RandCaseStatement', 'RandCaseStatementSyntax', 'RandJoinClauseSyntax', 'RandMode', 'RandSeqProductionSymbol', 'RandSequenceStatement', 'RandSequenceStatementSyntax', 'RangeCoverageBinInitializerSyntax', 'RangeDimensionSpecifierSyntax', 'RangeListSyntax', 'RangeSelectExpression', 'RangeSelectSyntax', 'RangeSelectionKind', 'RealLiteral', 'RepeatLoopStatement', 'RepeatedEventControl', 'RepeatedEventControlSyntax', 'ReplicatedAssignmentPatternExpression', 'ReplicatedAssignmentPatternSyntax', 'ReplicationExpression', 'ReportedDiagnostic', 'ReturnStatement', 'ReturnStatementSyntax', 'RootSymbol', 'RsCaseItemSyntax', 'RsCaseSyntax', 'RsCodeBlockSyntax', 'RsElseClauseSyntax', 'RsIfElseSyntax', 'RsProdItemSyntax', 'RsProdSyntax', 'RsRepeatSyntax', 'RsRuleSyntax', 'RsWeightClauseSyntax', 'SVInt', 'ScalarType', 'Scope', 'ScopedNameSyntax', 'ScriptSession', 'SelectorSyntax', 'SequenceConcatExpr', 'SequenceDeclarationSyntax', 'SequenceExprSyntax', 'SequenceMatchListSyntax', 'SequenceRange', 'SequenceRepetition', 'SequenceRepetitionSyntax', 'SequenceSymbol', 'SequenceType', 'SequenceWithMatchExpr', 'SetExprBinsSelectExpr', 'SignalEventControl', 'SignalEventExpressionSyntax', 'SignedCastExpressionSyntax', 'SimpleAssertionExpr', 'SimpleAssignmentPatternExpression', 'SimpleAssignmentPatternSyntax', 'SimpleBinsSelectExprSyntax', 'SimpleDirectiveSyntax', 'SimplePathSuffixSyntax', 'SimplePragmaExpressionSyntax', 'SimplePropertyExprSyntax', 'SimpleSequenceExprSyntax', 'SimpleSystemSubroutine', 'SolveBeforeConstraint', 'SolveBeforeConstraintSyntax', 'SourceBuffer', 'SourceLibrary', 'SourceLoader', 'SourceLocation', 'SourceManager', 'SourceOptions', 'SourceRange', 'SpecifyBlockSymbol', 'SpecifyBlockSyntax', 'SpecparamDeclarationSyntax', 'SpecparamDeclaratorSyntax', 'SpecparamSymbol', 'StandardCaseItemSyntax', 'StandardPropertyCaseItemSyntax', 'StandardRsCaseItemSyntax', 'Statement', 'StatementBlockKind', 'StatementBlockSymbol', 'StatementKind', 'StatementList', 'StatementSyntax', 'StreamExpressionSyntax', 'StreamExpressionWithRangeSyntax', 'StreamingConcatenationExpression', 'StreamingConcatenationExpressionSyntax', 'StringLiteral', 'StringType', 'StrongWeakAssertionExpr', 'StrongWeakPropertyExprSyntax', 'StructUnionMemberSyntax', 'StructUnionTypeSyntax', 'StructurePattern', 'StructurePatternMemberSyntax', 'StructurePatternSyntax', 'StructuredAssignmentPatternExpression', 'StructuredAssignmentPatternSyntax', 'SubroutineKind', 'SubroutineSymbol', 'SuperNewDefaultedArgsExpressionSyntax', 'Symbol', 'SymbolKind', 'SyntaxKind', 'SyntaxNode', 'SyntaxPrinter', 'SyntaxTree', 'SystemNameSyntax', 'SystemSubroutine', 'SystemTimingCheckKind', 'SystemTimingCheckSymbol', 'SystemTimingCheckSyntax', 'TaggedPattern', 'TaggedPatternSyntax', 'TaggedUnionExpression', 'TaggedUnionExpressionSyntax', 'TempVarSymbol', 'TextDiagnosticClient', 'TimeLiteral', 'TimeScale', 'TimeScaleDirectiveSyntax', 'TimeScaleMagnitude', 'TimeScaleValue', 'TimeUnit', 'TimeUnitsDeclarationSyntax', 'TimedStatement', 'TimingCheckArgSyntax', 'TimingCheckEventArgSyntax', 'TimingCheckEventConditionSyntax', 'TimingControl', 'TimingControlExpressionSyntax', 'TimingControlKind', 'TimingControlStatementSyntax', 'TimingControlSyntax', 'TimingPathSymbol', 'Token', 'TokenKind', 'TransListCoverageBinInitializerSyntax', 'TransRangeSyntax', 'TransRepeatRangeSyntax', 'TransSetSyntax', 'TransparentMemberSymbol', 'Trivia', 'TriviaKind', 'Type', 'TypeAliasType', 'TypeAssignmentSyntax', 'TypeParameterDeclarationSyntax', 'TypeParameterSymbol', 'TypePrinter', 'TypePrintingOptions', 'TypeRefType', 'TypeReferenceExpression', 'TypeReferenceSyntax', 'TypedefDeclarationSyntax', 'UdpBodySyntax', 'UdpDeclarationSyntax', 'UdpEdgeFieldSyntax', 'UdpEntrySyntax', 'UdpFieldBaseSyntax', 'UdpInitialStmtSyntax', 'UdpInputPortDeclSyntax', 'UdpOutputPortDeclSyntax', 'UdpPortDeclSyntax', 'UdpPortListSyntax', 'UdpSimpleFieldSyntax', 'UnaryAssertionExpr', 'UnaryAssertionOperator', 'UnaryBinsSelectExpr', 'UnaryBinsSelectExprSyntax', 'UnaryConditionalDirectiveExpressionSyntax', 'UnaryExpression', 'UnaryOperator', 'UnaryPropertyExprSyntax', 'UnarySelectPropertyExprSyntax', 'UnbasedUnsizedIntegerLiteral', 'Unbounded', 'UnboundedLiteral', 'UnboundedType', 'UnconditionalBranchDirectiveSyntax', 'UnconnectedDrive', 'UnconnectedDriveDirectiveSyntax', 'UndefDirectiveSyntax', 'UninstantiatedDefSymbol', 'UniquePriorityCheck', 'UniquenessConstraint', 'UniquenessConstraintSyntax', 'UnpackedStructType', 'UnpackedUnionType', 'UntypedType', 'UserDefinedNetDeclarationSyntax', 'ValueDriver', 'ValueExpressionBase', 'ValueRangeExpression', 'ValueRangeExpressionSyntax', 'ValueRangeKind', 'ValueSymbol', 'VariableDeclStatement', 'VariableDimensionSyntax', 'VariableFlags', 'VariableLifetime', 'VariablePattern', 'VariablePatternSyntax', 'VariablePortHeaderSyntax', 'VariableSymbol', 'VersionInfo', 'VirtualInterfaceType', 'VirtualInterfaceTypeSyntax', 'Visibility', 'VisitAction', 'VoidCastedCallStatementSyntax', 'VoidType', 'WaitForkStatement', 'WaitForkStatementSyntax', 'WaitOrderStatement', 'WaitOrderStatementSyntax', 'WaitStatement', 'WaitStatementSyntax', 'WhileLoopStatement', 'WildcardDimensionSpecifierSyntax', 'WildcardImportSymbol', 'WildcardPattern', 'WildcardPatternSyntax', 'WildcardPortConnectionSyntax', 'WildcardPortListSyntax', 'WildcardUdpPortListSyntax', 'WithClauseSyntax', 'WithFunctionClauseSyntax', 'WithFunctionSampleSyntax', 'clog2', 'literalBaseFromChar', 'logic_t']
class ASTContext:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, scope: ..., lookupLocation: ..., flags: ASTFlags = ...) -> None:
        ...
    def addAssertionBacktrace(self, diag: ...) -> None:
        ...
    @typing.overload
    def addDiag(self, code: ..., location: ...) -> ...:
        ...
    @typing.overload
    def addDiag(self, code: ..., sourceRange: ...) -> ...:
        ...
    def eval(self, expr: ..., extraFlags: EvalFlags = ...) -> ...:
        ...
    def evalDimension(self, syntax: ..., requireRange: bool, isPacked: bool) -> EvaluatedDimension:
        ...
    @typing.overload
    def evalInteger(self, syntax: ..., extraFlags: ASTFlags = ...) -> int | None:
        ...
    @typing.overload
    def evalInteger(self, expr: ..., extraFlags: EvalFlags = ...) -> int | None:
        ...
    @typing.overload
    def evalPackedDimension(self, syntax: ...) -> EvaluatedDimension:
        ...
    @typing.overload
    def evalPackedDimension(self, syntax: ...) -> EvaluatedDimension:
        ...
    def evalUnpackedDimension(self, syntax: ...) -> EvaluatedDimension:
        ...
    def getRandMode(self, symbol: ...) -> ...:
        ...
    def requireBooleanConvertible(self, expr: ...) -> bool:
        ...
    def requireGtZero(self, value: int | None, range: ...) -> bool:
        ...
    @typing.overload
    def requireIntegral(self, expr: ...) -> bool:
        ...
    @typing.overload
    def requireIntegral(self, cv: ..., range: ...) -> bool:
        ...
    def requireNoUnknowns(self, value: ..., range: ...) -> bool:
        ...
    @typing.overload
    def requirePositive(self, value: ..., range: ...) -> bool:
        ...
    @typing.overload
    def requirePositive(self, value: int | None, range: ...) -> bool:
        ...
    @typing.overload
    def requireSimpleExpr(self, expr: ...) -> ...:
        ...
    @typing.overload
    def requireSimpleExpr(self, expr: ..., code: ...) -> ...:
        ...
    @typing.overload
    def requireValidBitWidth(self, width: int, range: ...) -> bool:
        ...
    @typing.overload
    def requireValidBitWidth(self, value: ..., range: ...) -> int | None:
        ...
    def resetFlags(self, addedFlags: ASTFlags) -> ASTContext:
        ...
    def tryEval(self, expr: ...) -> ...:
        ...
    @property
    def flags(self) -> ASTFlags:
        ...
    @property
    def getCompilation(self) -> ...:
        ...
    @property
    def getContainingSubroutine(self) -> ...:
        ...
    @property
    def getDriverKind(self) -> ...:
        ...
    @property
    def getInstance(self) -> ...:
        ...
    @property
    def getLocation(self) -> ...:
        ...
    @property
    def getProceduralBlock(self) -> ...:
        ...
    @property
    def inAlwaysCombLatch(self) -> bool:
        ...
    @property
    def inUnevaluatedBranch(self) -> bool:
        ...
    @property
    def lookupIndex(self) -> ...:
        ...
    @property
    def scope(self) -> ...:
        ...
class ASTFlags:
    """
    Members:

      None_

      InsideConcatenation

      UnevaluatedBranch

      AllowDataType

      AssignmentAllowed

      AssignmentDisallowed

      NonProcedural

      StaticInitializer

      StreamingAllowed

      TopLevelStatement

      AllowUnboundedLiteral

      AllowUnboundedLiteralArithmetic

      Function

      Final

      NonBlockingTimingControl

      EventExpression

      AllowTypeReferences

      AssertionExpr

      AllowClockingBlock

      AssertionInstanceArgCheck

      AssertionDelayOrRepetition

      LValue

      PropertyNegation

      PropertyTimeAdvance

      RecursivePropertyArg

      ConcurrentAssertActionBlock

      AllowCoverageSampleFormal

      AllowCoverpoint

      AllowNetType

      OutputArg

      ProceduralAssign

      ProceduralForceRelease

      AllowInterconnect

      NotADriver

      StreamingWithRange

      SpecifyBlock

      SpecparamInitializer

      DPIArg

      AssertionDefaultArg

      LAndRValue

      NoReference

      ConfigParam

      TypeOperator

      ForkJoinAnyNone

      DisallowUDNT

      BindInstantiation
    """
    AllowClockingBlock: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowClockingBlock: 131072>
    AllowCoverageSampleFormal: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowCoverageSampleFormal: 33554432>
    AllowCoverpoint: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowCoverpoint: 67108864>
    AllowDataType: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowDataType: 4>
    AllowInterconnect: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowInterconnect: 2147483648>
    AllowNetType: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowNetType: 134217728>
    AllowTypeReferences: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowTypeReferences: 32768>
    AllowUnboundedLiteral: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowUnboundedLiteral: 512>
    AllowUnboundedLiteralArithmetic: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowUnboundedLiteralArithmetic: 1024>
    AssertionDefaultArg: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssertionDefaultArg: 137438953472>
    AssertionDelayOrRepetition: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssertionDelayOrRepetition: 524288>
    AssertionExpr: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssertionExpr: 65536>
    AssertionInstanceArgCheck: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssertionInstanceArgCheck: 262144>
    AssignmentAllowed: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssignmentAllowed: 8>
    AssignmentDisallowed: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssignmentDisallowed: 16>
    BindInstantiation: typing.ClassVar[ASTFlags]  # value = <ASTFlags.BindInstantiation: 17592186044416>
    ConcurrentAssertActionBlock: typing.ClassVar[ASTFlags]  # value = <ASTFlags.ConcurrentAssertActionBlock: 16777216>
    ConfigParam: typing.ClassVar[ASTFlags]  # value = <ASTFlags.ConfigParam: 1099511627776>
    DPIArg: typing.ClassVar[ASTFlags]  # value = <ASTFlags.DPIArg: 68719476736>
    DisallowUDNT: typing.ClassVar[ASTFlags]  # value = <ASTFlags.DisallowUDNT: 8796093022208>
    EventExpression: typing.ClassVar[ASTFlags]  # value = <ASTFlags.EventExpression: 16384>
    Final: typing.ClassVar[ASTFlags]  # value = <ASTFlags.Final: 4096>
    ForkJoinAnyNone: typing.ClassVar[ASTFlags]  # value = <ASTFlags.ForkJoinAnyNone: 4398046511104>
    Function: typing.ClassVar[ASTFlags]  # value = <ASTFlags.Function: 2048>
    InsideConcatenation: typing.ClassVar[ASTFlags]  # value = <ASTFlags.InsideConcatenation: 1>
    LAndRValue: typing.ClassVar[ASTFlags]  # value = <ASTFlags.LAndRValue: 274877906944>
    LValue: typing.ClassVar[ASTFlags]  # value = <ASTFlags.LValue: 1048576>
    NoReference: typing.ClassVar[ASTFlags]  # value = <ASTFlags.NoReference: 549755813888>
    NonBlockingTimingControl: typing.ClassVar[ASTFlags]  # value = <ASTFlags.NonBlockingTimingControl: 8192>
    NonProcedural: typing.ClassVar[ASTFlags]  # value = <ASTFlags.NonProcedural: 32>
    None_: typing.ClassVar[ASTFlags]  # value = <ASTFlags.None_: 0>
    NotADriver: typing.ClassVar[ASTFlags]  # value = <ASTFlags.NotADriver: 4294967296>
    OutputArg: typing.ClassVar[ASTFlags]  # value = <ASTFlags.OutputArg: 268435456>
    ProceduralAssign: typing.ClassVar[ASTFlags]  # value = <ASTFlags.ProceduralAssign: 536870912>
    ProceduralForceRelease: typing.ClassVar[ASTFlags]  # value = <ASTFlags.ProceduralForceRelease: 1073741824>
    PropertyNegation: typing.ClassVar[ASTFlags]  # value = <ASTFlags.PropertyNegation: 2097152>
    PropertyTimeAdvance: typing.ClassVar[ASTFlags]  # value = <ASTFlags.PropertyTimeAdvance: 4194304>
    RecursivePropertyArg: typing.ClassVar[ASTFlags]  # value = <ASTFlags.RecursivePropertyArg: 8388608>
    SpecifyBlock: typing.ClassVar[ASTFlags]  # value = <ASTFlags.SpecifyBlock: 17179869184>
    SpecparamInitializer: typing.ClassVar[ASTFlags]  # value = <ASTFlags.SpecparamInitializer: 34359738368>
    StaticInitializer: typing.ClassVar[ASTFlags]  # value = <ASTFlags.StaticInitializer: 64>
    StreamingAllowed: typing.ClassVar[ASTFlags]  # value = <ASTFlags.StreamingAllowed: 128>
    StreamingWithRange: typing.ClassVar[ASTFlags]  # value = <ASTFlags.StreamingWithRange: 8589934592>
    TopLevelStatement: typing.ClassVar[ASTFlags]  # value = <ASTFlags.TopLevelStatement: 256>
    TypeOperator: typing.ClassVar[ASTFlags]  # value = <ASTFlags.TypeOperator: 2199023255552>
    UnevaluatedBranch: typing.ClassVar[ASTFlags]  # value = <ASTFlags.UnevaluatedBranch: 2>
    __members__: typing.ClassVar[dict[str, ASTFlags]]  # value = {'None_': <ASTFlags.None_: 0>, 'InsideConcatenation': <ASTFlags.InsideConcatenation: 1>, 'UnevaluatedBranch': <ASTFlags.UnevaluatedBranch: 2>, 'AllowDataType': <ASTFlags.AllowDataType: 4>, 'AssignmentAllowed': <ASTFlags.AssignmentAllowed: 8>, 'AssignmentDisallowed': <ASTFlags.AssignmentDisallowed: 16>, 'NonProcedural': <ASTFlags.NonProcedural: 32>, 'StaticInitializer': <ASTFlags.StaticInitializer: 64>, 'StreamingAllowed': <ASTFlags.StreamingAllowed: 128>, 'TopLevelStatement': <ASTFlags.TopLevelStatement: 256>, 'AllowUnboundedLiteral': <ASTFlags.AllowUnboundedLiteral: 512>, 'AllowUnboundedLiteralArithmetic': <ASTFlags.AllowUnboundedLiteralArithmetic: 1024>, 'Function': <ASTFlags.Function: 2048>, 'Final': <ASTFlags.Final: 4096>, 'NonBlockingTimingControl': <ASTFlags.NonBlockingTimingControl: 8192>, 'EventExpression': <ASTFlags.EventExpression: 16384>, 'AllowTypeReferences': <ASTFlags.AllowTypeReferences: 32768>, 'AssertionExpr': <ASTFlags.AssertionExpr: 65536>, 'AllowClockingBlock': <ASTFlags.AllowClockingBlock: 131072>, 'AssertionInstanceArgCheck': <ASTFlags.AssertionInstanceArgCheck: 262144>, 'AssertionDelayOrRepetition': <ASTFlags.AssertionDelayOrRepetition: 524288>, 'LValue': <ASTFlags.LValue: 1048576>, 'PropertyNegation': <ASTFlags.PropertyNegation: 2097152>, 'PropertyTimeAdvance': <ASTFlags.PropertyTimeAdvance: 4194304>, 'RecursivePropertyArg': <ASTFlags.RecursivePropertyArg: 8388608>, 'ConcurrentAssertActionBlock': <ASTFlags.ConcurrentAssertActionBlock: 16777216>, 'AllowCoverageSampleFormal': <ASTFlags.AllowCoverageSampleFormal: 33554432>, 'AllowCoverpoint': <ASTFlags.AllowCoverpoint: 67108864>, 'AllowNetType': <ASTFlags.AllowNetType: 134217728>, 'OutputArg': <ASTFlags.OutputArg: 268435456>, 'ProceduralAssign': <ASTFlags.ProceduralAssign: 536870912>, 'ProceduralForceRelease': <ASTFlags.ProceduralForceRelease: 1073741824>, 'AllowInterconnect': <ASTFlags.AllowInterconnect: 2147483648>, 'NotADriver': <ASTFlags.NotADriver: 4294967296>, 'StreamingWithRange': <ASTFlags.StreamingWithRange: 8589934592>, 'SpecifyBlock': <ASTFlags.SpecifyBlock: 17179869184>, 'SpecparamInitializer': <ASTFlags.SpecparamInitializer: 34359738368>, 'DPIArg': <ASTFlags.DPIArg: 68719476736>, 'AssertionDefaultArg': <ASTFlags.AssertionDefaultArg: 137438953472>, 'LAndRValue': <ASTFlags.LAndRValue: 274877906944>, 'NoReference': <ASTFlags.NoReference: 549755813888>, 'ConfigParam': <ASTFlags.ConfigParam: 1099511627776>, 'TypeOperator': <ASTFlags.TypeOperator: 2199023255552>, 'ForkJoinAnyNone': <ASTFlags.ForkJoinAnyNone: 4398046511104>, 'DisallowUDNT': <ASTFlags.DisallowUDNT: 8796093022208>, 'BindInstantiation': <ASTFlags.BindInstantiation: 17592186044416>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class AbortAssertionExpr(AssertionExpr):
    class Action:
        """
        Members:

          Accept

          Reject
        """
        Accept: typing.ClassVar[AbortAssertionExpr.Action]  # value = <Action.Accept: 0>
        Reject: typing.ClassVar[AbortAssertionExpr.Action]  # value = <Action.Reject: 1>
        __members__: typing.ClassVar[dict[str, AbortAssertionExpr.Action]]  # value = {'Accept': <Action.Accept: 0>, 'Reject': <Action.Reject: 1>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Accept: typing.ClassVar[AbortAssertionExpr.Action]  # value = <Action.Accept: 0>
    Reject: typing.ClassVar[AbortAssertionExpr.Action]  # value = <Action.Reject: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def action(self) -> ...:
        ...
    @property
    def condition(self) -> ...:
        ...
    @property
    def expr(self) -> AssertionExpr:
        ...
    @property
    def isSync(self) -> bool:
        ...
class AcceptOnPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    expr: PropertyExprSyntax
    keyword: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ActionBlockSyntax(SyntaxNode):
    elseClause: ElseClauseSyntax
    statement: StatementSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AnonymousProgramSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AnonymousProgramSyntax(MemberSyntax):
    endkeyword: Token
    keyword: Token
    members: ...
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AnsiPortListSyntax(PortListSyntax):
    closeParen: Token
    openParen: Token
    ports: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AnsiUdpPortListSyntax(UdpPortListSyntax):
    closeParen: Token
    openParen: Token
    ports: ...
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ArbitrarySymbolExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def symbol(self) -> ...:
        ...
class ArgumentDirection:
    """
    Members:

      In

      Out

      InOut

      Ref
    """
    In: typing.ClassVar[ArgumentDirection]  # value = <ArgumentDirection.In: 0>
    InOut: typing.ClassVar[ArgumentDirection]  # value = <ArgumentDirection.InOut: 2>
    Out: typing.ClassVar[ArgumentDirection]  # value = <ArgumentDirection.Out: 1>
    Ref: typing.ClassVar[ArgumentDirection]  # value = <ArgumentDirection.Ref: 3>
    __members__: typing.ClassVar[dict[str, ArgumentDirection]]  # value = {'In': <ArgumentDirection.In: 0>, 'Out': <ArgumentDirection.Out: 1>, 'InOut': <ArgumentDirection.InOut: 2>, 'Ref': <ArgumentDirection.Ref: 3>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ArgumentListSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    parameters: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ArgumentSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ArrayOrRandomizeMethodExpressionSyntax(ExpressionSyntax):
    args: ParenExpressionListSyntax
    constraints: ConstraintBlockSyntax
    method: ExpressionSyntax
    with: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AssertionExpr:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __repr__(self) -> str:
        ...
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> AssertionExprKind:
        ...
    @property
    def syntax(self) -> ...:
        ...
class AssertionExprKind:
    """
    Members:

      Invalid

      Simple

      SequenceConcat

      SequenceWithMatch

      Unary

      Binary

      FirstMatch

      Clocking

      StrongWeak

      Abort

      Conditional

      Case

      DisableIff
    """
    Abort: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Abort: 9>
    Binary: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Binary: 5>
    Case: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Case: 11>
    Clocking: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Clocking: 7>
    Conditional: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Conditional: 10>
    DisableIff: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.DisableIff: 12>
    FirstMatch: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.FirstMatch: 6>
    Invalid: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Invalid: 0>
    SequenceConcat: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.SequenceConcat: 2>
    SequenceWithMatch: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.SequenceWithMatch: 3>
    Simple: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Simple: 1>
    StrongWeak: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.StrongWeak: 8>
    Unary: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Unary: 4>
    __members__: typing.ClassVar[dict[str, AssertionExprKind]]  # value = {'Invalid': <AssertionExprKind.Invalid: 0>, 'Simple': <AssertionExprKind.Simple: 1>, 'SequenceConcat': <AssertionExprKind.SequenceConcat: 2>, 'SequenceWithMatch': <AssertionExprKind.SequenceWithMatch: 3>, 'Unary': <AssertionExprKind.Unary: 4>, 'Binary': <AssertionExprKind.Binary: 5>, 'FirstMatch': <AssertionExprKind.FirstMatch: 6>, 'Clocking': <AssertionExprKind.Clocking: 7>, 'StrongWeak': <AssertionExprKind.StrongWeak: 8>, 'Abort': <AssertionExprKind.Abort: 9>, 'Conditional': <AssertionExprKind.Conditional: 10>, 'Case': <AssertionExprKind.Case: 11>, 'DisableIff': <AssertionExprKind.DisableIff: 12>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class AssertionInstanceExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arguments(self) -> span[tuple[..., Expression | AssertionExpr | TimingControl]]:
        ...
    @property
    def body(self) -> AssertionExpr:
        ...
    @property
    def isRecursiveProperty(self) -> bool:
        ...
    @property
    def localVars(self) -> span[...]:
        ...
    @property
    def symbol(self) -> ...:
        ...
class AssertionItemPortListSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    ports: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AssertionItemPortSyntax(SyntaxNode):
    attributes: ...
    defaultValue: EqualsAssertionArgClauseSyntax
    dimensions: ...
    direction: Token
    local: Token
    name: Token
    type: DataTypeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AssertionKind:
    """
    Members:

      Assert

      Assume

      CoverProperty

      CoverSequence

      Restrict

      Expect
    """
    Assert: typing.ClassVar[AssertionKind]  # value = <AssertionKind.Assert: 0>
    Assume: typing.ClassVar[AssertionKind]  # value = <AssertionKind.Assume: 1>
    CoverProperty: typing.ClassVar[AssertionKind]  # value = <AssertionKind.CoverProperty: 2>
    CoverSequence: typing.ClassVar[AssertionKind]  # value = <AssertionKind.CoverSequence: 3>
    Expect: typing.ClassVar[AssertionKind]  # value = <AssertionKind.Expect: 5>
    Restrict: typing.ClassVar[AssertionKind]  # value = <AssertionKind.Restrict: 4>
    __members__: typing.ClassVar[dict[str, AssertionKind]]  # value = {'Assert': <AssertionKind.Assert: 0>, 'Assume': <AssertionKind.Assume: 1>, 'CoverProperty': <AssertionKind.CoverProperty: 2>, 'CoverSequence': <AssertionKind.CoverSequence: 3>, 'Restrict': <AssertionKind.Restrict: 4>, 'Expect': <AssertionKind.Expect: 5>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class AssertionPortSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def direction(self) -> ArgumentDirection | None:
        ...
    @property
    def isLocalVar(self) -> bool:
        ...
    @property
    def type(self) -> ...:
        ...
class AssignmentExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def isCompound(self) -> bool:
        ...
    @property
    def isLValueArg(self) -> bool:
        ...
    @property
    def isNonBlocking(self) -> bool:
        ...
    @property
    def left(self) -> Expression:
        ...
    @property
    def op(self) -> BinaryOperator | None:
        ...
    @property
    def right(self) -> Expression:
        ...
    @property
    def timingControl(self) -> TimingControl:
        ...
class AssignmentPatternExpressionBase(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def elements(self) -> span[Expression]:
        ...
class AssignmentPatternExpressionSyntax(PrimaryExpressionSyntax):
    pattern: AssignmentPatternSyntax
    type: DataTypeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AssignmentPatternItemSyntax(SyntaxNode):
    colon: Token
    expr: ExpressionSyntax
    key: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AssignmentPatternSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AssociativeArrayType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def elementType(self) -> Type:
        ...
    @property
    def indexType(self) -> Type:
        ...
class AttributeInstanceSyntax(SyntaxNode):
    closeParen: Token
    closeStar: Token
    openParen: Token
    openStar: Token
    specs: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AttributeSpecSyntax(SyntaxNode):
    name: Token
    value: EqualsValueClauseSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class AttributeSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def value(self) -> ConstantValue:
        ...
class BadExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class Bag:
    compilationOptions: CompilationOptions
    lexerOptions: ...
    parserOptions: ...
    preprocessorOptions: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, list: list) -> None:
        ...
class BeginKeywordsDirectiveSyntax(DirectiveSyntax):
    versionSpecifier: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BinSelectWithFilterExpr(BinsSelectExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> BinsSelectExpr:
        ...
    @property
    def filter(self) -> ...:
        ...
    @property
    def matchesExpr(self) -> ...:
        ...
class BinSelectWithFilterExprSyntax(BinsSelectExpressionSyntax):
    closeParen: Token
    expr: BinsSelectExpressionSyntax
    filter: ExpressionSyntax
    matchesClause: MatchesClauseSyntax
    openParen: Token
    with: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BinaryAssertionExpr(AssertionExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def left(self) -> AssertionExpr:
        ...
    @property
    def op(self) -> BinaryAssertionOperator:
        ...
    @property
    def right(self) -> AssertionExpr:
        ...
class BinaryAssertionOperator:
    """
    Members:

      And

      Or

      Intersect

      Throughout

      Within

      Iff

      Until

      SUntil

      UntilWith

      SUntilWith

      Implies

      OverlappedImplication

      NonOverlappedImplication

      OverlappedFollowedBy

      NonOverlappedFollowedBy
    """
    And: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.And: 0>
    Iff: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Iff: 5>
    Implies: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Implies: 10>
    Intersect: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Intersect: 2>
    NonOverlappedFollowedBy: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.NonOverlappedFollowedBy: 14>
    NonOverlappedImplication: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.NonOverlappedImplication: 12>
    Or: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Or: 1>
    OverlappedFollowedBy: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.OverlappedFollowedBy: 13>
    OverlappedImplication: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.OverlappedImplication: 11>
    SUntil: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.SUntil: 7>
    SUntilWith: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.SUntilWith: 9>
    Throughout: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Throughout: 3>
    Until: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Until: 6>
    UntilWith: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.UntilWith: 8>
    Within: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Within: 4>
    __members__: typing.ClassVar[dict[str, BinaryAssertionOperator]]  # value = {'And': <BinaryAssertionOperator.And: 0>, 'Or': <BinaryAssertionOperator.Or: 1>, 'Intersect': <BinaryAssertionOperator.Intersect: 2>, 'Throughout': <BinaryAssertionOperator.Throughout: 3>, 'Within': <BinaryAssertionOperator.Within: 4>, 'Iff': <BinaryAssertionOperator.Iff: 5>, 'Until': <BinaryAssertionOperator.Until: 6>, 'SUntil': <BinaryAssertionOperator.SUntil: 7>, 'UntilWith': <BinaryAssertionOperator.UntilWith: 8>, 'SUntilWith': <BinaryAssertionOperator.SUntilWith: 9>, 'Implies': <BinaryAssertionOperator.Implies: 10>, 'OverlappedImplication': <BinaryAssertionOperator.OverlappedImplication: 11>, 'NonOverlappedImplication': <BinaryAssertionOperator.NonOverlappedImplication: 12>, 'OverlappedFollowedBy': <BinaryAssertionOperator.OverlappedFollowedBy: 13>, 'NonOverlappedFollowedBy': <BinaryAssertionOperator.NonOverlappedFollowedBy: 14>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BinaryBinsSelectExpr(BinsSelectExpr):
    class Op:
        """
        Members:

          And

          Or
        """
        And: typing.ClassVar[BinaryBinsSelectExpr.Op]  # value = <Op.And: 0>
        Or: typing.ClassVar[BinaryBinsSelectExpr.Op]  # value = <Op.Or: 1>
        __members__: typing.ClassVar[dict[str, BinaryBinsSelectExpr.Op]]  # value = {'And': <Op.And: 0>, 'Or': <Op.Or: 1>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    And: typing.ClassVar[BinaryBinsSelectExpr.Op]  # value = <Op.And: 0>
    Or: typing.ClassVar[BinaryBinsSelectExpr.Op]  # value = <Op.Or: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def left(self) -> BinsSelectExpr:
        ...
    @property
    def op(self) -> ...:
        ...
    @property
    def right(self) -> BinsSelectExpr:
        ...
class BinaryBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    left: BinsSelectExpressionSyntax
    op: Token
    right: BinsSelectExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BinaryBlockEventExpressionSyntax(BlockEventExpressionSyntax):
    left: BlockEventExpressionSyntax
    orKeyword: Token
    right: BlockEventExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BinaryConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    left: ConditionalDirectiveExpressionSyntax
    op: Token
    right: ConditionalDirectiveExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BinaryEventExpressionSyntax(EventExpressionSyntax):
    left: EventExpressionSyntax
    operatorToken: Token
    right: EventExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BinaryExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def left(self) -> Expression:
        ...
    @property
    def op(self) -> BinaryOperator:
        ...
    @property
    def right(self) -> Expression:
        ...
class BinaryExpressionSyntax(ExpressionSyntax):
    attributes: ...
    left: ExpressionSyntax
    operatorToken: Token
    right: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BinaryOperator:
    """
    Members:

      Add

      Subtract

      Multiply

      Divide

      Mod

      BinaryAnd

      BinaryOr

      BinaryXor

      BinaryXnor

      Equality

      Inequality

      CaseEquality

      CaseInequality

      GreaterThanEqual

      GreaterThan

      LessThanEqual

      LessThan

      WildcardEquality

      WildcardInequality

      LogicalAnd

      LogicalOr

      LogicalImplication

      LogicalEquivalence

      LogicalShiftLeft

      LogicalShiftRight

      ArithmeticShiftLeft

      ArithmeticShiftRight

      Power
    """
    Add: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Add: 0>
    ArithmeticShiftLeft: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.ArithmeticShiftLeft: 25>
    ArithmeticShiftRight: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.ArithmeticShiftRight: 26>
    BinaryAnd: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.BinaryAnd: 5>
    BinaryOr: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.BinaryOr: 6>
    BinaryXnor: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.BinaryXnor: 8>
    BinaryXor: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.BinaryXor: 7>
    CaseEquality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.CaseEquality: 11>
    CaseInequality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.CaseInequality: 12>
    Divide: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Divide: 3>
    Equality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Equality: 9>
    GreaterThan: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.GreaterThan: 14>
    GreaterThanEqual: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.GreaterThanEqual: 13>
    Inequality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Inequality: 10>
    LessThan: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LessThan: 16>
    LessThanEqual: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LessThanEqual: 15>
    LogicalAnd: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalAnd: 19>
    LogicalEquivalence: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalEquivalence: 22>
    LogicalImplication: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalImplication: 21>
    LogicalOr: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalOr: 20>
    LogicalShiftLeft: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalShiftLeft: 23>
    LogicalShiftRight: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalShiftRight: 24>
    Mod: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Mod: 4>
    Multiply: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Multiply: 2>
    Power: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Power: 27>
    Subtract: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Subtract: 1>
    WildcardEquality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.WildcardEquality: 17>
    WildcardInequality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.WildcardInequality: 18>
    __members__: typing.ClassVar[dict[str, BinaryOperator]]  # value = {'Add': <BinaryOperator.Add: 0>, 'Subtract': <BinaryOperator.Subtract: 1>, 'Multiply': <BinaryOperator.Multiply: 2>, 'Divide': <BinaryOperator.Divide: 3>, 'Mod': <BinaryOperator.Mod: 4>, 'BinaryAnd': <BinaryOperator.BinaryAnd: 5>, 'BinaryOr': <BinaryOperator.BinaryOr: 6>, 'BinaryXor': <BinaryOperator.BinaryXor: 7>, 'BinaryXnor': <BinaryOperator.BinaryXnor: 8>, 'Equality': <BinaryOperator.Equality: 9>, 'Inequality': <BinaryOperator.Inequality: 10>, 'CaseEquality': <BinaryOperator.CaseEquality: 11>, 'CaseInequality': <BinaryOperator.CaseInequality: 12>, 'GreaterThanEqual': <BinaryOperator.GreaterThanEqual: 13>, 'GreaterThan': <BinaryOperator.GreaterThan: 14>, 'LessThanEqual': <BinaryOperator.LessThanEqual: 15>, 'LessThan': <BinaryOperator.LessThan: 16>, 'WildcardEquality': <BinaryOperator.WildcardEquality: 17>, 'WildcardInequality': <BinaryOperator.WildcardInequality: 18>, 'LogicalAnd': <BinaryOperator.LogicalAnd: 19>, 'LogicalOr': <BinaryOperator.LogicalOr: 20>, 'LogicalImplication': <BinaryOperator.LogicalImplication: 21>, 'LogicalEquivalence': <BinaryOperator.LogicalEquivalence: 22>, 'LogicalShiftLeft': <BinaryOperator.LogicalShiftLeft: 23>, 'LogicalShiftRight': <BinaryOperator.LogicalShiftRight: 24>, 'ArithmeticShiftLeft': <BinaryOperator.ArithmeticShiftLeft: 25>, 'ArithmeticShiftRight': <BinaryOperator.ArithmeticShiftRight: 26>, 'Power': <BinaryOperator.Power: 27>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BinaryPropertyExprSyntax(PropertyExprSyntax):
    left: PropertyExprSyntax
    op: Token
    right: PropertyExprSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BinarySequenceExprSyntax(SequenceExprSyntax):
    left: SequenceExprSyntax
    op: Token
    right: SequenceExprSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BindDirectiveSyntax(MemberSyntax):
    bind: Token
    instantiation: MemberSyntax
    target: NameSyntax
    targetInstances: BindTargetListSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BindTargetListSyntax(SyntaxNode):
    colon: Token
    targets: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BinsSelectConditionExprSyntax(BinsSelectExpressionSyntax):
    binsof: Token
    closeParen: Token
    intersects: IntersectClauseSyntax
    name: NameSyntax
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BinsSelectExpr:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __repr__(self) -> str:
        ...
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> BinsSelectExprKind:
        ...
    @property
    def syntax(self) -> ...:
        ...
class BinsSelectExprKind:
    """
    Members:

      Invalid

      Condition

      Unary

      Binary

      SetExpr

      WithFilter

      CrossId
    """
    Binary: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.Binary: 3>
    Condition: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.Condition: 1>
    CrossId: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.CrossId: 6>
    Invalid: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.Invalid: 0>
    SetExpr: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.SetExpr: 4>
    Unary: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.Unary: 2>
    WithFilter: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.WithFilter: 5>
    __members__: typing.ClassVar[dict[str, BinsSelectExprKind]]  # value = {'Invalid': <BinsSelectExprKind.Invalid: 0>, 'Condition': <BinsSelectExprKind.Condition: 1>, 'Unary': <BinsSelectExprKind.Unary: 2>, 'Binary': <BinsSelectExprKind.Binary: 3>, 'SetExpr': <BinsSelectExprKind.SetExpr: 4>, 'WithFilter': <BinsSelectExprKind.WithFilter: 5>, 'CrossId': <BinsSelectExprKind.CrossId: 6>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BinsSelectExpressionSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BinsSelectionSyntax(MemberSyntax):
    equals: Token
    expr: BinsSelectExpressionSyntax
    iff: CoverageIffClauseSyntax
    keyword: Token
    name: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BitSelectSyntax(SelectorSyntax):
    expr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BlockCoverageEventSyntax(SyntaxNode):
    atat: Token
    closeParen: Token
    expr: BlockEventExpressionSyntax
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BlockEventExpressionSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BlockEventListControl(TimingControl):
    class Event:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def isBegin(self) -> bool:
            ...
        @property
        def target(self) -> ...:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def events(self) -> span[...]:
        ...
class BlockStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def blockKind(self) -> StatementBlockKind:
        ...
    @property
    def blockSymbol(self) -> ...:
        ...
    @property
    def body(self) -> Statement:
        ...
class BlockStatementSyntax(StatementSyntax):
    begin: Token
    blockName: NamedBlockClauseSyntax
    end: Token
    endBlockName: NamedBlockClauseSyntax
    items: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BreakStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class BufferID:
    placeholder: typing.ClassVar[BufferID]  # value = BufferID(4294967295)
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def getPlaceholder() -> BufferID:
        ...
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: BufferID) -> bool:
        ...
    def __ge__(self, arg0: BufferID) -> bool:
        ...
    def __gt__(self, arg0: BufferID) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __init__(self) -> None:
        ...
    def __le__(self, arg0: BufferID) -> bool:
        ...
    def __lt__(self, arg0: BufferID) -> bool:
        ...
    def __ne__(self, arg0: BufferID) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def id(self) -> int:
        ...
class BumpAllocator:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
class CHandleType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CallExpression(Expression):
    class IteratorCallInfo:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def iterExpr(self) -> Expression:
            ...
        @property
        def iterVar(self) -> ...:
            ...
    class RandomizeCallInfo:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def constraintRestrictions(self) -> span[str]:
            ...
        @property
        def inlineConstraints(self) -> Constraint:
            ...
    class SystemCallInfo:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def extraInfo(self) -> None | CallExpression.IteratorCallInfo | CallExpression.RandomizeCallInfo:
            ...
        @property
        def scope(self) -> ...:
            ...
        @property
        def subroutine(self) -> SystemSubroutine:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arguments(self) -> span[Expression]:
        ...
    @property
    def isSystemCall(self) -> bool:
        ...
    @property
    def subroutine(self) -> ... | ...:
        ...
    @property
    def subroutineKind(self) -> SubroutineKind:
        ...
    @property
    def subroutineName(self) -> str:
        ...
    @property
    def thisClass(self) -> Expression:
        ...
class CaseAssertionExpr(AssertionExpr):
    class ItemGroup:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def body(self) -> AssertionExpr:
            ...
        @property
        def expressions(self) -> span[...]:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def defaultCase(self) -> AssertionExpr:
        ...
    @property
    def expr(self) -> ...:
        ...
    @property
    def items(self) -> span[...]:
        ...
class CaseGenerateSyntax(MemberSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    endCase: Token
    items: ...
    keyword: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CaseItemSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CasePropertyExprSyntax(PropertyExprSyntax):
    caseKeyword: Token
    closeParen: Token
    endcase: Token
    expr: ExpressionSyntax
    items: ...
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CaseStatement(Statement):
    class ItemGroup:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def expressions(self) -> span[Expression]:
            ...
        @property
        def stmt(self) -> Statement:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def check(self) -> UniquePriorityCheck:
        ...
    @property
    def condition(self) -> CaseStatementCondition:
        ...
    @property
    def defaultCase(self) -> Statement:
        ...
    @property
    def expr(self) -> Expression:
        ...
    @property
    def items(self) -> span[...]:
        ...
class CaseStatementCondition:
    """
    Members:

      Normal

      WildcardXOrZ

      WildcardJustZ

      Inside
    """
    Inside: typing.ClassVar[CaseStatementCondition]  # value = <CaseStatementCondition.Inside: 3>
    Normal: typing.ClassVar[CaseStatementCondition]  # value = <CaseStatementCondition.Normal: 0>
    WildcardJustZ: typing.ClassVar[CaseStatementCondition]  # value = <CaseStatementCondition.WildcardJustZ: 2>
    WildcardXOrZ: typing.ClassVar[CaseStatementCondition]  # value = <CaseStatementCondition.WildcardXOrZ: 1>
    __members__: typing.ClassVar[dict[str, CaseStatementCondition]]  # value = {'Normal': <CaseStatementCondition.Normal: 0>, 'WildcardXOrZ': <CaseStatementCondition.WildcardXOrZ: 1>, 'WildcardJustZ': <CaseStatementCondition.WildcardJustZ: 2>, 'Inside': <CaseStatementCondition.Inside: 3>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CaseStatementSyntax(StatementSyntax):
    caseKeyword: Token
    closeParen: Token
    endcase: Token
    expr: ExpressionSyntax
    items: ...
    matchesOrInside: Token
    openParen: Token
    uniqueOrPriority: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CastExpressionSyntax(ExpressionSyntax):
    apostrophe: Token
    left: ExpressionSyntax
    right: ParenthesizedExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CellConfigRuleSyntax(ConfigRuleSyntax):
    cell: Token
    name: ConfigCellIdentifierSyntax
    ruleClause: ConfigRuleClauseSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ChargeStrengthSyntax(NetStrengthSyntax):
    closeParen: Token
    openParen: Token
    strength: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CheckerDataDeclarationSyntax(MemberSyntax):
    data: DataDeclarationSyntax
    rand: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CheckerDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    keyword: Token
    members: ...
    name: Token
    portList: AssertionItemPortListSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CheckerInstanceBodySymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def checker(self) -> ...:
        ...
    @property
    def parentInstance(self) -> CheckerInstanceSymbol:
        ...
class CheckerInstanceStatementSyntax(StatementSyntax):
    instance: CheckerInstantiationSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CheckerInstanceSymbol(InstanceSymbolBase):
    class Connection:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def actual(self) -> Expression | AssertionExpr | TimingControl:
            ...
        @property
        def attributes(self) -> span[AttributeSymbol]:
            ...
        @property
        def formal(self) -> Symbol:
            ...
        @property
        def outputInitialExpr(self) -> Expression:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def body(self) -> ...:
        ...
    @property
    def portConnections(self) -> span[...]:
        ...
class CheckerInstantiationSyntax(MemberSyntax):
    instances: ...
    parameters: ParameterValueAssignmentSyntax
    semi: Token
    type: NameSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CheckerSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def ports(self) -> span[AssertionPortSymbol]:
        ...
class ClassDeclarationSyntax(MemberSyntax):
    classKeyword: Token
    endBlockName: NamedBlockClauseSyntax
    endClass: Token
    extendsClause: ExtendsClauseSyntax
    finalSpecifier: ClassSpecifierSyntax
    implementsClause: ImplementsClauseSyntax
    items: ...
    name: Token
    parameters: ParameterPortListSyntax
    semi: Token
    virtualOrInterface: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ClassMethodDeclarationSyntax(MemberSyntax):
    declaration: FunctionDeclarationSyntax
    qualifiers: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ClassMethodPrototypeSyntax(MemberSyntax):
    prototype: FunctionPrototypeSyntax
    qualifiers: ...
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ClassNameSyntax(NameSyntax):
    identifier: Token
    parameters: ParameterValueAssignmentSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ClassPropertyDeclarationSyntax(MemberSyntax):
    declaration: MemberSyntax
    qualifiers: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ClassPropertySymbol(VariableSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def randMode(self) -> RandMode:
        ...
    @property
    def visibility(self) -> Visibility:
        ...
class ClassSpecifierSyntax(SyntaxNode):
    colon: Token
    keyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ClassType(Type, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def baseClass(self) -> Type:
        ...
    @property
    def baseConstructorCall(self) -> Expression:
        ...
    @property
    def constructor(self) -> SubroutineSymbol:
        ...
    @property
    def firstForwardDecl(self) -> ForwardingTypedefSymbol:
        ...
    @property
    def genericClass(self) -> ...:
        ...
    @property
    def implementedInterfaces(self) -> span[Type]:
        ...
    @property
    def isAbstract(self) -> bool:
        ...
    @property
    def isFinal(self) -> bool:
        ...
    @property
    def isInterface(self) -> bool:
        ...
class ClockVarSymbol(VariableSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def direction(self) -> ArgumentDirection:
        ...
    @property
    def inputSkew(self) -> ClockingSkew:
        ...
    @property
    def outputSkew(self) -> ClockingSkew:
        ...
class ClockingAssertionExpr(AssertionExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def clocking(self) -> TimingControl:
        ...
    @property
    def expr(self) -> AssertionExpr:
        ...
class ClockingBlockSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def defaultInputSkew(self) -> ClockingSkew:
        ...
    @property
    def defaultOutputSkew(self) -> ClockingSkew:
        ...
    @property
    def event(self) -> TimingControl:
        ...
class ClockingDeclarationSyntax(MemberSyntax):
    at: Token
    blockName: Token
    clocking: Token
    endBlockName: NamedBlockClauseSyntax
    endClocking: Token
    event: EventExpressionSyntax
    globalOrDefault: Token
    items: ...
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ClockingDirectionSyntax(SyntaxNode):
    input: Token
    inputSkew: ClockingSkewSyntax
    output: Token
    outputSkew: ClockingSkewSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ClockingEventExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def timingControl(self) -> TimingControl:
        ...
class ClockingItemSyntax(MemberSyntax):
    decls: ...
    direction: ClockingDirectionSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ClockingPropertyExprSyntax(PropertyExprSyntax):
    event: TimingControlSyntax
    expr: PropertyExprSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ClockingSequenceExprSyntax(SequenceExprSyntax):
    event: TimingControlSyntax
    expr: SequenceExprSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ClockingSkew:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def delay(self) -> TimingControl:
        ...
    @property
    def edge(self) -> EdgeKind:
        ...
    @property
    def hasValue(self) -> bool:
        ...
class ClockingSkewSyntax(SyntaxNode):
    delay: TimingControlSyntax
    edge: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ColonExpressionClauseSyntax(SyntaxNode):
    colon: Token
    expr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CommandLineOptions:
    expandEnvVars: bool
    ignoreDuplicates: bool
    ignoreProgramName: bool
    supportsComments: bool
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
class Compilation:
    class DefinitionLookupResult:
        configRoot: ...
        configRule: ...
        definition: ...
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __init__(self) -> None:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, options: ...) -> None:
        ...
    def addDiagnostics(self, diagnostics: ...) -> None:
        ...
    def addSyntaxTree(self, tree: ...) -> None:
        ...
    def addSystemMethod(self, typeKind: ..., method: ...) -> None:
        ...
    def addSystemSubroutine(self, subroutine: ...) -> None:
        ...
    def createScriptScope(self) -> ...:
        ...
    def getAllDiagnostics(self) -> ...:
        ...
    @typing.overload
    def getAttributes(self, symbol: ...) -> span[...]:
        ...
    @typing.overload
    def getAttributes(self, stmt: ...) -> span[...]:
        ...
    @typing.overload
    def getAttributes(self, expr: ...) -> span[...]:
        ...
    @typing.overload
    def getAttributes(self, conn: ...) -> span[...]:
        ...
    def getCompilationUnit(self, syntax: ...) -> ...:
        ...
    def getCompilationUnits(self) -> span[...]:
        ...
    def getDefinitions(self) -> list[...]:
        ...
    def getGateType(self, name: str) -> ...:
        ...
    def getNetType(self, kind: ...) -> ...:
        ...
    def getPackage(self, name: str) -> ...:
        ...
    def getPackages(self) -> list[...]:
        ...
    def getParseDiagnostics(self) -> ...:
        ...
    def getRoot(self) -> ...:
        ...
    def getSemanticDiagnostics(self) -> ...:
        ...
    def getSourceLibrary(self, name: str) -> ...:
        ...
    def getStdPackage(self) -> ...:
        ...
    def getSyntaxTrees(self) -> span[...]:
        ...
    def getSystemMethod(self, typeKind: ..., name: str) -> ...:
        ...
    def getSystemSubroutine(self, name: str) -> ...:
        ...
    def getType(self, kind: ...) -> ...:
        ...
    def parseName(self, name: str) -> ...:
        ...
    def tryGetDefinition(self, name: str, scope: ...) -> ...:
        ...
    def tryParseName(self, name: str, diags: ...) -> ...:
        ...
    @property
    def bitType(self) -> ...:
        ...
    @property
    def byteType(self) -> ...:
        ...
    @property
    def defaultLibrary(self) -> ...:
        ...
    @property
    def defaultTimeScale(self) -> ... | None:
        ...
    @property
    def errorType(self) -> ...:
        ...
    @property
    def hasIssuedErrors(self) -> bool:
        ...
    @property
    def intType(self) -> ...:
        ...
    @property
    def integerType(self) -> ...:
        ...
    @property
    def isFinalized(self) -> bool:
        ...
    @property
    def logicType(self) -> ...:
        ...
    @property
    def nullType(self) -> ...:
        ...
    @property
    def options(self) -> CompilationOptions:
        ...
    @property
    def realType(self) -> ...:
        ...
    @property
    def shortRealType(self) -> ...:
        ...
    @property
    def sourceManager(self) -> ...:
        ...
    @property
    def stringType(self) -> ...:
        ...
    @property
    def typeRefType(self) -> ...:
        ...
    @property
    def unboundedType(self) -> ...:
        ...
    @property
    def unsignedIntType(self) -> ...:
        ...
    @property
    def voidType(self) -> ...:
        ...
    @property
    def wireNetType(self) -> ...:
        ...
class CompilationFlags:
    """
    Members:

      None_

      AllowHierarchicalConst

      RelaxEnumConversions

      AllowUseBeforeDeclare

      AllowDupInitialDrivers

      AllowTopLevelIfacePorts

      StrictDriverChecking

      LintMode

      SuppressUnused

      IgnoreUnknownModules

      RelaxStringConversions

      AllowRecursiveImplicitCall

      AllowBareValParamAssignment

      AllowSelfDeterminedStreamConcat

      AllowMultiDrivenLocals

      AllowMergingAnsiPorts
    """
    AllowBareValParamAssignment: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowBareValParamAssignment: 2048>
    AllowDupInitialDrivers: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowDupInitialDrivers: 8>
    AllowHierarchicalConst: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowHierarchicalConst: 1>
    AllowMergingAnsiPorts: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowMergingAnsiPorts: 16384>
    AllowMultiDrivenLocals: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowMultiDrivenLocals: 8192>
    AllowRecursiveImplicitCall: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowRecursiveImplicitCall: 1024>
    AllowSelfDeterminedStreamConcat: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowSelfDeterminedStreamConcat: 4096>
    AllowTopLevelIfacePorts: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowTopLevelIfacePorts: 16>
    AllowUseBeforeDeclare: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowUseBeforeDeclare: 4>
    IgnoreUnknownModules: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.IgnoreUnknownModules: 256>
    LintMode: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.LintMode: 64>
    None_: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.None_: 0>
    RelaxEnumConversions: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.RelaxEnumConversions: 2>
    RelaxStringConversions: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.RelaxStringConversions: 512>
    StrictDriverChecking: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.StrictDriverChecking: 32>
    SuppressUnused: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.SuppressUnused: 128>
    __members__: typing.ClassVar[dict[str, CompilationFlags]]  # value = {'None_': <CompilationFlags.None_: 0>, 'AllowHierarchicalConst': <CompilationFlags.AllowHierarchicalConst: 1>, 'RelaxEnumConversions': <CompilationFlags.RelaxEnumConversions: 2>, 'AllowUseBeforeDeclare': <CompilationFlags.AllowUseBeforeDeclare: 4>, 'AllowDupInitialDrivers': <CompilationFlags.AllowDupInitialDrivers: 8>, 'AllowTopLevelIfacePorts': <CompilationFlags.AllowTopLevelIfacePorts: 16>, 'StrictDriverChecking': <CompilationFlags.StrictDriverChecking: 32>, 'LintMode': <CompilationFlags.LintMode: 64>, 'SuppressUnused': <CompilationFlags.SuppressUnused: 128>, 'IgnoreUnknownModules': <CompilationFlags.IgnoreUnknownModules: 256>, 'RelaxStringConversions': <CompilationFlags.RelaxStringConversions: 512>, 'AllowRecursiveImplicitCall': <CompilationFlags.AllowRecursiveImplicitCall: 1024>, 'AllowBareValParamAssignment': <CompilationFlags.AllowBareValParamAssignment: 2048>, 'AllowSelfDeterminedStreamConcat': <CompilationFlags.AllowSelfDeterminedStreamConcat: 4096>, 'AllowMultiDrivenLocals': <CompilationFlags.AllowMultiDrivenLocals: 8192>, 'AllowMergingAnsiPorts': <CompilationFlags.AllowMergingAnsiPorts: 16384>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CompilationOptions:
    defaultLiblist: list[str]
    defaultTimeScale: ... | None
    errorLimit: int
    flags: CompilationFlags
    languageVersion: ...
    maxConstexprBacktrace: int
    maxConstexprDepth: int
    maxConstexprSteps: int
    maxDefParamSteps: int
    maxGenerateSteps: int
    maxInstanceArray: int
    maxInstanceDepth: int
    minTypMax: MinTypMax
    paramOverrides: list[str]
    topModules: set[str]
    typoCorrectionLimit: int
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
class CompilationUnitSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def timeScale(self) -> TimeScale | None:
        ...
class CompilationUnitSyntax(SyntaxNode):
    endOfFile: Token
    members: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConcatenationExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def operands(self) -> span[Expression]:
        ...
class ConcatenationExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    expressions: ...
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConcurrentAssertionMemberSyntax(MemberSyntax):
    statement: ConcurrentAssertionStatementSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConcurrentAssertionStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def assertionKind(self) -> AssertionKind:
        ...
    @property
    def ifFalse(self) -> Statement:
        ...
    @property
    def ifTrue(self) -> Statement:
        ...
    @property
    def propertySpec(self) -> AssertionExpr:
        ...
class ConcurrentAssertionStatementSyntax(StatementSyntax):
    action: ActionBlockSyntax
    closeParen: Token
    keyword: Token
    openParen: Token
    propertyOrSequence: Token
    propertySpec: PropertySpecSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConditionBinsSelectExpr(BinsSelectExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def intersects(self) -> span[...]:
        ...
    @property
    def target(self) -> ...:
        ...
class ConditionalAssertionExpr(AssertionExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def condition(self) -> ...:
        ...
    @property
    def elseExpr(self) -> AssertionExpr:
        ...
    @property
    def ifExpr(self) -> AssertionExpr:
        ...
class ConditionalBranchDirectiveSyntax(DirectiveSyntax):
    disabledTokens: ...
    expr: ConditionalDirectiveExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConditionalConstraint(Constraint):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def elseBody(self) -> Constraint:
        ...
    @property
    def ifBody(self) -> Constraint:
        ...
    @property
    def predicate(self) -> ...:
        ...
class ConditionalConstraintSyntax(ConstraintItemSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    constraints: ConstraintItemSyntax
    elseClause: ElseConstraintClauseSyntax
    ifKeyword: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConditionalDirectiveExpressionSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConditionalExpression(Expression):
    class Condition:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def pattern(self) -> Pattern:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def conditions(self) -> span[...]:
        ...
    @property
    def left(self) -> Expression:
        ...
    @property
    def right(self) -> Expression:
        ...
class ConditionalExpressionSyntax(ExpressionSyntax):
    attributes: ...
    colon: Token
    left: ExpressionSyntax
    predicate: ConditionalPredicateSyntax
    question: Token
    right: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConditionalPathDeclarationSyntax(MemberSyntax):
    closeParen: Token
    keyword: Token
    openParen: Token
    path: PathDeclarationSyntax
    predicate: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConditionalPatternSyntax(SyntaxNode):
    expr: ExpressionSyntax
    matchesClause: MatchesClauseSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConditionalPredicateSyntax(SyntaxNode):
    conditions: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConditionalPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    elseClause: ElsePropertyClauseSyntax
    expr: PropertyExprSyntax
    ifKeyword: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConditionalStatement(Statement):
    class Condition:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def pattern(self) -> Pattern:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def check(self) -> UniquePriorityCheck:
        ...
    @property
    def conditions(self) -> span[...]:
        ...
    @property
    def ifFalse(self) -> Statement:
        ...
    @property
    def ifTrue(self) -> Statement:
        ...
class ConditionalStatementSyntax(StatementSyntax):
    closeParen: Token
    elseClause: ElseClauseSyntax
    ifKeyword: Token
    openParen: Token
    predicate: ConditionalPredicateSyntax
    statement: StatementSyntax
    uniqueOrPriority: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConfigBlockSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConfigCellIdentifierSyntax(SyntaxNode):
    cell: Token
    dot: Token
    library: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConfigDeclarationSyntax(MemberSyntax):
    blockName: NamedBlockClauseSyntax
    config: Token
    design: Token
    endconfig: Token
    localparams: ...
    name: Token
    rules: ...
    semi1: Token
    semi2: Token
    topCells: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConfigInstanceIdentifierSyntax(SyntaxNode):
    dot: Token
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConfigLiblistSyntax(ConfigRuleClauseSyntax):
    liblist: Token
    libraries: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConfigRuleClauseSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConfigRuleSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConfigUseClauseSyntax(ConfigRuleClauseSyntax):
    colon: Token
    config: Token
    name: ConfigCellIdentifierSyntax
    paramAssignments: ParameterValueAssignmentSyntax
    use: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConstantPattern(Pattern):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> ...:
        ...
class ConstantRange:
    __hash__: typing.ClassVar[None] = None
    left: int
    right: int
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, arg0: ConstantRange) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, left: int, right: int) -> None:
        ...
    def __ne__(self, arg0: ConstantRange) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def containsPoint(self, arg0: int) -> bool:
        ...
    def getIndexedRange(self: int, arg0: int, arg1: bool, arg2: bool) -> ConstantRange | None:
        ...
    def overlaps(self, arg0: ConstantRange) -> bool:
        ...
    def reverse(self) -> ConstantRange:
        ...
    def subrange(self, arg0: ConstantRange) -> ConstantRange:
        ...
    def translateIndex(self, arg0: int) -> int:
        ...
    @property
    def isLittleEndian(self) -> bool:
        ...
    @property
    def lower(self) -> int:
        ...
    @property
    def upper(self) -> int:
        ...
    @property
    def width(self) -> int:
        ...
class ConstantValue:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: ConstantValue) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, integer: SVInt) -> None:
        ...
    @typing.overload
    def __init__(self, str: str) -> None:
        ...
    @typing.overload
    def __init__(self, value: int) -> None:
        ...
    @typing.overload
    def __init__(self, value: float) -> None:
        ...
    def __ne__(self, arg0: ConstantValue) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def bitstreamWidth(self) -> int:
        ...
    def convertToByteArray(self, size: int, isSigned: bool) -> ConstantValue:
        ...
    def convertToByteQueue(self, isSigned: bool) -> ConstantValue:
        ...
    @typing.overload
    def convertToInt(self) -> ConstantValue:
        ...
    @typing.overload
    def convertToInt(self, width: int, isSigned: bool, isFourState: bool) -> ConstantValue:
        ...
    def convertToReal(self) -> ConstantValue:
        ...
    def convertToShortReal(self) -> ConstantValue:
        ...
    def convertToStr(self) -> ConstantValue:
        ...
    def empty(self) -> bool:
        ...
    def getSlice(self, upper: int, lower: int, defaultValue: ConstantValue) -> ConstantValue:
        ...
    def hasUnknown(self) -> bool:
        ...
    def isContainer(self) -> bool:
        ...
    def isFalse(self) -> bool:
        ...
    def isTrue(self) -> bool:
        ...
    def size(self) -> int:
        ...
    @property
    def value(self) -> typing.Any:
        ...
class Constraint:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __repr__(self) -> str:
        ...
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> ConstraintKind:
        ...
    @property
    def syntax(self) -> ...:
        ...
class ConstraintBlockFlags:
    """
    Members:

      None_

      Pure

      Static

      Extern

      ExplicitExtern

      Initial

      Extends

      Final
    """
    ExplicitExtern: typing.ClassVar[ConstraintBlockFlags]  # value = <ConstraintBlockFlags.ExplicitExtern: 16>
    Extends: typing.ClassVar[ConstraintBlockFlags]  # value = <ConstraintBlockFlags.Extends: 64>
    Extern: typing.ClassVar[ConstraintBlockFlags]  # value = <ConstraintBlockFlags.Extern: 8>
    Final: typing.ClassVar[ConstraintBlockFlags]  # value = <ConstraintBlockFlags.Final: 128>
    Initial: typing.ClassVar[ConstraintBlockFlags]  # value = <ConstraintBlockFlags.Initial: 32>
    None_: typing.ClassVar[ConstraintBlockFlags]  # value = <ConstraintBlockFlags.None_: 0>
    Pure: typing.ClassVar[ConstraintBlockFlags]  # value = <ConstraintBlockFlags.Pure: 2>
    Static: typing.ClassVar[ConstraintBlockFlags]  # value = <ConstraintBlockFlags.Static: 4>
    __members__: typing.ClassVar[dict[str, ConstraintBlockFlags]]  # value = {'None_': <ConstraintBlockFlags.None_: 0>, 'Pure': <ConstraintBlockFlags.Pure: 2>, 'Static': <ConstraintBlockFlags.Static: 4>, 'Extern': <ConstraintBlockFlags.Extern: 8>, 'ExplicitExtern': <ConstraintBlockFlags.ExplicitExtern: 16>, 'Initial': <ConstraintBlockFlags.Initial: 32>, 'Extends': <ConstraintBlockFlags.Extends: 64>, 'Final': <ConstraintBlockFlags.Final: 128>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ConstraintBlockSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def constraints(self) -> Constraint:
        ...
    @property
    def flags(self) -> ConstraintBlockFlags:
        ...
    @property
    def thisVar(self) -> VariableSymbol:
        ...
class ConstraintBlockSyntax(ConstraintItemSyntax):
    closeBrace: Token
    items: ...
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConstraintDeclarationSyntax(MemberSyntax):
    block: ConstraintBlockSyntax
    keyword: Token
    name: NameSyntax
    qualifiers: ...
    specifiers: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConstraintItemSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConstraintKind:
    """
    Members:

      Invalid

      List

      Expression

      Implication

      Conditional

      Uniqueness

      DisableSoft

      SolveBefore

      Foreach
    """
    Conditional: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Conditional: 4>
    DisableSoft: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.DisableSoft: 6>
    Expression: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Expression: 2>
    Foreach: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Foreach: 8>
    Implication: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Implication: 3>
    Invalid: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Invalid: 0>
    List: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.List: 1>
    SolveBefore: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.SolveBefore: 7>
    Uniqueness: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Uniqueness: 5>
    __members__: typing.ClassVar[dict[str, ConstraintKind]]  # value = {'Invalid': <ConstraintKind.Invalid: 0>, 'List': <ConstraintKind.List: 1>, 'Expression': <ConstraintKind.Expression: 2>, 'Implication': <ConstraintKind.Implication: 3>, 'Conditional': <ConstraintKind.Conditional: 4>, 'Uniqueness': <ConstraintKind.Uniqueness: 5>, 'DisableSoft': <ConstraintKind.DisableSoft: 6>, 'SolveBefore': <ConstraintKind.SolveBefore: 7>, 'Foreach': <ConstraintKind.Foreach: 8>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ConstraintList(Constraint):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def list(self) -> span[Constraint]:
        ...
class ConstraintPrototypeSyntax(MemberSyntax):
    keyword: Token
    name: NameSyntax
    qualifiers: ...
    semi: Token
    specifiers: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ContinueStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ContinuousAssignSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def assignment(self) -> Expression:
        ...
    @property
    def delay(self) -> TimingControl:
        ...
    @property
    def driveStrength(self) -> tuple[... | None, ... | None]:
        ...
class ContinuousAssignSyntax(MemberSyntax):
    assign: Token
    assignments: ...
    delay: TimingControlSyntax
    semi: Token
    strength: DriveStrengthSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ConversionExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def conversionKind(self) -> ConversionKind:
        ...
    @property
    def isImplicit(self) -> bool:
        ...
    @property
    def operand(self) -> Expression:
        ...
class ConversionKind:
    """
    Members:

      Implicit

      Propagated

      StreamingConcat

      Explicit

      BitstreamCast
    """
    BitstreamCast: typing.ClassVar[ConversionKind]  # value = <ConversionKind.BitstreamCast: 4>
    Explicit: typing.ClassVar[ConversionKind]  # value = <ConversionKind.Explicit: 3>
    Implicit: typing.ClassVar[ConversionKind]  # value = <ConversionKind.Implicit: 0>
    Propagated: typing.ClassVar[ConversionKind]  # value = <ConversionKind.Propagated: 1>
    StreamingConcat: typing.ClassVar[ConversionKind]  # value = <ConversionKind.StreamingConcat: 2>
    __members__: typing.ClassVar[dict[str, ConversionKind]]  # value = {'Implicit': <ConversionKind.Implicit: 0>, 'Propagated': <ConversionKind.Propagated: 1>, 'StreamingConcat': <ConversionKind.StreamingConcat: 2>, 'Explicit': <ConversionKind.Explicit: 3>, 'BitstreamCast': <ConversionKind.BitstreamCast: 4>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CopyClassExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def sourceExpr(self) -> Expression:
        ...
class CopyClassExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    scopedNew: NameSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CoverCrossBodySymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def crossQueueType(self) -> ...:
        ...
class CoverCrossSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def iffExpr(self) -> Expression:
        ...
    @property
    def options(self) -> span[CoverageOptionSetter]:
        ...
    @property
    def targets(self) -> span[CoverpointSymbol]:
        ...
class CoverCrossSyntax(MemberSyntax):
    closeBrace: Token
    cross: Token
    emptySemi: Token
    iff: CoverageIffClauseSyntax
    items: ...
    label: NamedLabelSyntax
    members: ...
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CoverageBinInitializerSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CoverageBinSymbol(Symbol):
    class BinKind:
        """
        Members:

          Bins

          IllegalBins

          IgnoreBins
        """
        Bins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.Bins: 0>
        IgnoreBins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.IgnoreBins: 2>
        IllegalBins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.IllegalBins: 1>
        __members__: typing.ClassVar[dict[str, CoverageBinSymbol.BinKind]]  # value = {'Bins': <BinKind.Bins: 0>, 'IllegalBins': <BinKind.IllegalBins: 1>, 'IgnoreBins': <BinKind.IgnoreBins: 2>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class TransRangeList:
        class RepeatKind:
            """
            Members:

              None_

              Consecutive

              Nonconsecutive

              GoTo
            """
            Consecutive: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.Consecutive: 1>
            GoTo: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.GoTo: 3>
            Nonconsecutive: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.Nonconsecutive: 2>
            None_: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.None_: 0>
            __members__: typing.ClassVar[dict[str, CoverageBinSymbol.TransRangeList.RepeatKind]]  # value = {'None_': <RepeatKind.None_: 0>, 'Consecutive': <RepeatKind.Consecutive: 1>, 'Nonconsecutive': <RepeatKind.Nonconsecutive: 2>, 'GoTo': <RepeatKind.GoTo: 3>}
            @staticmethod
            def _pybind11_conduit_v1_(*args, **kwargs):
                ...
            def __eq__(self, other: typing.Any) -> bool:
                ...
            def __getstate__(self) -> int:
                ...
            def __hash__(self) -> int:
                ...
            def __index__(self) -> int:
                ...
            def __init__(self, value: int) -> None:
                ...
            def __int__(self) -> int:
                ...
            def __ne__(self, other: typing.Any) -> bool:
                ...
            def __repr__(self) -> str:
                ...
            def __setstate__(self, state: int) -> None:
                ...
            def __str__(self) -> str:
                ...
            @property
            def name(self) -> str:
                ...
            @property
            def value(self) -> int:
                ...
        Consecutive: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.Consecutive: 1>
        GoTo: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.GoTo: 3>
        Nonconsecutive: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.Nonconsecutive: 2>
        None_: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.None_: 0>
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def items(self) -> span[Expression]:
            ...
        @property
        def repeatFrom(self) -> Expression:
            ...
        @property
        def repeatKind(self) -> ...:
            ...
        @property
        def repeatTo(self) -> Expression:
            ...
    Bins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.Bins: 0>
    IgnoreBins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.IgnoreBins: 2>
    IllegalBins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.IllegalBins: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def binsKind(self) -> ...:
        ...
    @property
    def crossSelectExpr(self) -> BinsSelectExpr:
        ...
    @property
    def iffExpr(self) -> Expression:
        ...
    @property
    def isArray(self) -> bool:
        ...
    @property
    def isDefault(self) -> bool:
        ...
    @property
    def isDefaultSequence(self) -> bool:
        ...
    @property
    def isWildcard(self) -> bool:
        ...
    @property
    def numberOfBinsExpr(self) -> Expression:
        ...
    @property
    def setCoverageExpr(self) -> Expression:
        ...
    @property
    def values(self) -> span[Expression]:
        ...
    @property
    def withExpr(self) -> Expression:
        ...
class CoverageBinsArraySizeSyntax(SyntaxNode):
    closeBracket: Token
    expr: ExpressionSyntax
    openBracket: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CoverageBinsSyntax(MemberSyntax):
    equals: Token
    iff: CoverageIffClauseSyntax
    initializer: CoverageBinInitializerSyntax
    keyword: Token
    name: Token
    semi: Token
    size: CoverageBinsArraySizeSyntax
    wildcard: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CoverageIffClauseSyntax(SyntaxNode):
    closeParen: Token
    expr: ExpressionSyntax
    iff: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CoverageOptionSetter:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expression(self) -> Expression:
        ...
    @property
    def isTypeOption(self) -> bool:
        ...
    @property
    def name(self) -> str:
        ...
class CoverageOptionSyntax(MemberSyntax):
    expr: ExpressionSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CovergroupBodySymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def options(self) -> span[CoverageOptionSetter]:
        ...
class CovergroupDeclarationSyntax(MemberSyntax):
    covergroup: Token
    endBlockName: NamedBlockClauseSyntax
    endgroup: Token
    event: SyntaxNode
    extends: Token
    members: ...
    name: Token
    portList: FunctionPortListSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CovergroupType(Type, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arguments(self) -> span[FormalArgumentSymbol]:
        ...
    @property
    def baseGroup(self) -> Type:
        ...
    @property
    def body(self) -> CovergroupBodySymbol:
        ...
    @property
    def coverageEvent(self) -> TimingControl:
        ...
class CoverpointSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def coverageExpr(self) -> Expression:
        ...
    @property
    def iffExpr(self) -> Expression:
        ...
    @property
    def options(self) -> span[CoverageOptionSetter]:
        ...
    @property
    def type(self) -> ...:
        ...
class CoverpointSyntax(MemberSyntax):
    closeBrace: Token
    coverpoint: Token
    emptySemi: Token
    expr: ExpressionSyntax
    iff: CoverageIffClauseSyntax
    label: NamedLabelSyntax
    members: ...
    openBrace: Token
    type: DataTypeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CrossIdBinsSelectExpr(BinsSelectExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class CycleDelayControl(TimingControl):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> ...:
        ...
class DPIExportSyntax(MemberSyntax):
    c_identifier: Token
    equals: Token
    functionOrTask: Token
    keyword: Token
    name: Token
    semi: Token
    specString: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DPIImportSyntax(MemberSyntax):
    c_identifier: Token
    equals: Token
    keyword: Token
    method: FunctionPrototypeSyntax
    property: Token
    semi: Token
    specString: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DPIOpenArrayType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def elementType(self) -> Type:
        ...
    @property
    def isPacked(self) -> bool:
        ...
class DataDeclarationSyntax(MemberSyntax):
    declarators: ...
    modifiers: ...
    semi: Token
    type: DataTypeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DataTypeExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DataTypeSyntax(ExpressionSyntax):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DeclaratorSyntax(SyntaxNode):
    dimensions: ...
    initializer: EqualsValueClauseSyntax
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DeclaredType:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def initializer(self) -> Expression:
        ...
    @property
    def initializerLocation(self) -> SourceLocation:
        ...
    @property
    def initializerSyntax(self) -> ExpressionSyntax:
        ...
    @property
    def isEvaluating(self) -> bool:
        ...
    @property
    def type(self) -> Type:
        ...
    @property
    def typeSyntax(self) -> DataTypeSyntax:
        ...
class DefParamAssignmentSyntax(SyntaxNode):
    name: NameSyntax
    setter: EqualsValueClauseSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefParamSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def initializer(self) -> Expression:
        ...
    @property
    def target(self) -> Symbol:
        ...
    @property
    def value(self) -> ConstantValue:
        ...
class DefParamSyntax(MemberSyntax):
    assignments: ...
    defparam: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultCaseItemSyntax(CaseItemSyntax):
    clause: SyntaxNode
    colon: Token
    defaultKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultClockingReferenceSyntax(MemberSyntax):
    clocking: Token
    defaultKeyword: Token
    name: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultConfigRuleSyntax(ConfigRuleSyntax):
    defaultKeyword: Token
    liblist: ConfigLiblistSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    defaultKeyword: Token
    sequenceKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultDecayTimeDirectiveSyntax(DirectiveSyntax):
    time: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultDisableDeclarationSyntax(MemberSyntax):
    defaultKeyword: Token
    disableKeyword: Token
    expr: ExpressionSyntax
    iffKeyword: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultDistItemSyntax(DistItemBaseSyntax):
    defaultKeyword: Token
    weight: DistWeightSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultExtendsClauseArgSyntax(SyntaxNode):
    closeParen: Token
    defaultKeyword: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultFunctionPortSyntax(FunctionPortBaseSyntax):
    keyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultNetTypeDirectiveSyntax(DirectiveSyntax):
    netType: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultPropertyCaseItemSyntax(PropertyCaseItemSyntax):
    colon: Token
    defaultKeyword: Token
    expr: PropertyExprSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultRsCaseItemSyntax(RsCaseItemSyntax):
    colon: Token
    defaultKeyword: Token
    item: RsProdItemSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultSkewItemSyntax(MemberSyntax):
    direction: ClockingDirectionSyntax
    keyword: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefaultTriregStrengthDirectiveSyntax(DirectiveSyntax):
    strength: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DeferredAssertionSyntax(SyntaxNode):
    finalKeyword: Token
    hash: Token
    zero: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefineDirectiveSyntax(DirectiveSyntax):
    body: ...
    formalArguments: MacroFormalArgumentListSyntax
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DefinitionKind:
    """
    Members:

      Module

      Interface

      Program
    """
    Interface: typing.ClassVar[DefinitionKind]  # value = <DefinitionKind.Interface: 1>
    Module: typing.ClassVar[DefinitionKind]  # value = <DefinitionKind.Module: 0>
    Program: typing.ClassVar[DefinitionKind]  # value = <DefinitionKind.Program: 2>
    __members__: typing.ClassVar[dict[str, DefinitionKind]]  # value = {'Module': <DefinitionKind.Module: 0>, 'Interface': <DefinitionKind.Interface: 1>, 'Program': <DefinitionKind.Program: 2>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DefinitionSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __repr__(self) -> str:
        ...
    def getArticleKindString(self) -> str:
        ...
    def getKindString(self) -> str:
        ...
    @property
    def defaultLifetime(self) -> VariableLifetime:
        ...
    @property
    def defaultNetType(self) -> ...:
        ...
    @property
    def definitionKind(self) -> DefinitionKind:
        ...
    @property
    def instanceCount(self) -> int:
        ...
    @property
    def timeScale(self) -> TimeScale | None:
        ...
    @property
    def unconnectedDrive(self) -> UnconnectedDrive:
        ...
class Delay3Control(TimingControl):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr1(self) -> ...:
        ...
    @property
    def expr2(self) -> ...:
        ...
    @property
    def expr3(self) -> ...:
        ...
class Delay3Syntax(TimingControlSyntax):
    closeParen: Token
    comma1: Token
    comma2: Token
    delay1: ExpressionSyntax
    delay2: ExpressionSyntax
    delay3: ExpressionSyntax
    hash: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DelayControl(TimingControl):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> ...:
        ...
class DelaySyntax(TimingControlSyntax):
    delayValue: ExpressionSyntax
    hash: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DelayedSequenceElementSyntax(SyntaxNode):
    closeBracket: Token
    delayVal: ExpressionSyntax
    doubleHash: Token
    expr: SequenceExprSyntax
    op: Token
    openBracket: Token
    range: SelectorSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DelayedSequenceExprSyntax(SequenceExprSyntax):
    elements: ...
    first: SequenceExprSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DiagCode:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: DiagCode) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, subsystem: DiagSubsystem, code: int) -> None:
        ...
    def __ne__(self, arg0: DiagCode) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def getCode(self) -> int:
        ...
    def getSubsystem(self) -> DiagSubsystem:
        ...
class DiagGroup:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, name: str, diags: list[DiagCode]) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def getDiags(self) -> span[DiagCode]:
        ...
    def getName(self) -> str:
        ...
class DiagSubsystem:
    """
    Members:

      Invalid

      General

      Lexer

      Numeric

      Preprocessor

      Parser

      Declarations

      Expressions

      Statements

      Types

      Lookup

      SysFuncs

      ConstEval

      Compilation

      Meta

      Tidy

      Netlist
    """
    Compilation: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Compilation: 13>
    ConstEval: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.ConstEval: 12>
    Declarations: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Declarations: 6>
    Expressions: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Expressions: 7>
    General: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.General: 1>
    Invalid: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Invalid: 0>
    Lexer: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Lexer: 2>
    Lookup: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Lookup: 10>
    Meta: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Meta: 14>
    Netlist: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Netlist: 16>
    Numeric: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Numeric: 3>
    Parser: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Parser: 5>
    Preprocessor: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Preprocessor: 4>
    Statements: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Statements: 8>
    SysFuncs: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.SysFuncs: 11>
    Tidy: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Tidy: 15>
    Types: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Types: 9>
    __members__: typing.ClassVar[dict[str, DiagSubsystem]]  # value = {'Invalid': <DiagSubsystem.Invalid: 0>, 'General': <DiagSubsystem.General: 1>, 'Lexer': <DiagSubsystem.Lexer: 2>, 'Numeric': <DiagSubsystem.Numeric: 3>, 'Preprocessor': <DiagSubsystem.Preprocessor: 4>, 'Parser': <DiagSubsystem.Parser: 5>, 'Declarations': <DiagSubsystem.Declarations: 6>, 'Expressions': <DiagSubsystem.Expressions: 7>, 'Statements': <DiagSubsystem.Statements: 8>, 'Types': <DiagSubsystem.Types: 9>, 'Lookup': <DiagSubsystem.Lookup: 10>, 'SysFuncs': <DiagSubsystem.SysFuncs: 11>, 'ConstEval': <DiagSubsystem.ConstEval: 12>, 'Compilation': <DiagSubsystem.Compilation: 13>, 'Meta': <DiagSubsystem.Meta: 14>, 'Tidy': <DiagSubsystem.Tidy: 15>, 'Netlist': <DiagSubsystem.Netlist: 16>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Diagnostic:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, arg0: Diagnostic) -> bool:
        ...
    def __init__(self, code: DiagCode, location: SourceLocation) -> None:
        ...
    def __ne__(self, arg0: Diagnostic) -> bool:
        ...
    def isError(self) -> bool:
        ...
    @property
    def args(self) -> list[str | int | int | str | ConstantValue | tuple[..., ...]]:
        ...
    @property
    def code(self) -> DiagCode:
        ...
    @property
    def location(self) -> SourceLocation:
        ...
    @property
    def ranges(self) -> list[SourceRange]:
        ...
    @property
    def symbol(self) -> ...:
        ...
class DiagnosticClient:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def report(self, diagnostic: ReportedDiagnostic) -> None:
        ...
    def setEngine(self, engine: DiagnosticEngine) -> None:
        ...
class DiagnosticEngine:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def reportAll(sourceManager: SourceManager, diag: span[Diagnostic]) -> str:
        ...
    def __init__(self, sourceManager: SourceManager) -> None:
        ...
    def addClient(self, client: ...) -> None:
        ...
    def clearClients(self) -> None:
        ...
    def clearCounts(self) -> None:
        ...
    @typing.overload
    def clearMappings(self) -> None:
        ...
    @typing.overload
    def clearMappings(self, severity: DiagnosticSeverity) -> None:
        ...
    def findDiagGroup(self, name: str) -> DiagGroup:
        ...
    def findFromOptionName(self, optionName: str) -> span[DiagCode]:
        ...
    def formatMessage(self, diag: Diagnostic) -> str:
        ...
    def getMessage(self, code: DiagCode) -> str:
        ...
    def getOptionName(self, code: DiagCode) -> str:
        ...
    def getSeverity(self, code: DiagCode, location: SourceLocation) -> DiagnosticSeverity:
        ...
    def issue(self, diagnostic: Diagnostic) -> None:
        ...
    def setDefaultWarnings(self) -> None:
        ...
    def setErrorLimit(self, limit: int) -> None:
        ...
    def setErrorsAsFatal(self, set: bool) -> None:
        ...
    def setFatalsAsErrors(self, set: bool) -> None:
        ...
    def setIgnoreAllNotes(self, set: bool) -> None:
        ...
    def setIgnoreAllWarnings(self, set: bool) -> None:
        ...
    @typing.overload
    def setMappingsFromPragmas(self) -> Diagnostics:
        ...
    @typing.overload
    def setMappingsFromPragmas(self, buffer: BufferID) -> Diagnostics:
        ...
    def setMessage(self, code: DiagCode, message: str) -> None:
        ...
    @typing.overload
    def setSeverity(self, code: DiagCode, severity: DiagnosticSeverity) -> None:
        ...
    @typing.overload
    def setSeverity(self, group: DiagGroup, severity: DiagnosticSeverity) -> None:
        ...
    def setWarningOptions(self, options: span[str]) -> Diagnostics:
        ...
    def setWarningsAsErrors(self, set: bool) -> None:
        ...
    @property
    def numErrors(self) -> int:
        ...
    @property
    def numWarnings(self) -> int:
        ...
    @property
    def sourceManager(self) -> SourceManager:
        ...
class DiagnosticSeverity:
    """
    Members:

      Ignored

      Note

      Warning

      Error

      Fatal
    """
    Error: typing.ClassVar[DiagnosticSeverity]  # value = <DiagnosticSeverity.Error: 3>
    Fatal: typing.ClassVar[DiagnosticSeverity]  # value = <DiagnosticSeverity.Fatal: 4>
    Ignored: typing.ClassVar[DiagnosticSeverity]  # value = <DiagnosticSeverity.Ignored: 0>
    Note: typing.ClassVar[DiagnosticSeverity]  # value = <DiagnosticSeverity.Note: 1>
    Warning: typing.ClassVar[DiagnosticSeverity]  # value = <DiagnosticSeverity.Warning: 2>
    __members__: typing.ClassVar[dict[str, DiagnosticSeverity]]  # value = {'Ignored': <DiagnosticSeverity.Ignored: 0>, 'Note': <DiagnosticSeverity.Note: 1>, 'Warning': <DiagnosticSeverity.Warning: 2>, 'Error': <DiagnosticSeverity.Error: 3>, 'Fatal': <DiagnosticSeverity.Fatal: 4>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Diagnostics:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __getitem__(self, arg0: int) -> Diagnostic:
        ...
    def __init__(self) -> None:
        ...
    def __iter__(self) -> typing.Iterator[Diagnostic]:
        ...
    def __len__(self) -> int:
        ...
    @typing.overload
    def add(self, code: DiagCode, location: SourceLocation) -> Diagnostic:
        ...
    @typing.overload
    def add(self, code: DiagCode, range: SourceRange) -> Diagnostic:
        ...
    @typing.overload
    def add(self, source: ..., code: DiagCode, location: SourceLocation) -> Diagnostic:
        ...
    @typing.overload
    def add(self, source: ..., code: DiagCode, range: SourceRange) -> Diagnostic:
        ...
    def sort(self, sourceManager: SourceManager) -> None:
        ...
class Diags:
    AlwaysFFEventControl: typing.ClassVar[DiagCode]  # value = DiagCode(AlwaysFFEventControl)
    AlwaysInChecker: typing.ClassVar[DiagCode]  # value = DiagCode(AlwaysInChecker)
    AmbiguousWildcardImport: typing.ClassVar[DiagCode]  # value = DiagCode(AmbiguousWildcardImport)
    AnsiIfacePortDefault: typing.ClassVar[DiagCode]  # value = DiagCode(AnsiIfacePortDefault)
    ArgCannotBeEmpty: typing.ClassVar[DiagCode]  # value = DiagCode(ArgCannotBeEmpty)
    ArgDoesNotExist: typing.ClassVar[DiagCode]  # value = DiagCode(ArgDoesNotExist)
    ArithInShift: typing.ClassVar[DiagCode]  # value = DiagCode(ArithInShift)
    ArithOpMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(ArithOpMismatch)
    ArrayDimTooLarge: typing.ClassVar[DiagCode]  # value = DiagCode(ArrayDimTooLarge)
    ArrayLocatorWithClause: typing.ClassVar[DiagCode]  # value = DiagCode(ArrayLocatorWithClause)
    ArrayMethodComparable: typing.ClassVar[DiagCode]  # value = DiagCode(ArrayMethodComparable)
    ArrayMethodIntegral: typing.ClassVar[DiagCode]  # value = DiagCode(ArrayMethodIntegral)
    AssertionArgNeedsRegExpr: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionArgNeedsRegExpr)
    AssertionArgTypeMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionArgTypeMismatch)
    AssertionArgTypeSequence: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionArgTypeSequence)
    AssertionDelayFormalType: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionDelayFormalType)
    AssertionExprType: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionExprType)
    AssertionFuncArg: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionFuncArg)
    AssertionOutputLocalVar: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionOutputLocalVar)
    AssertionPortDirNoLocal: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionPortDirNoLocal)
    AssertionPortOutputDefault: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionPortOutputDefault)
    AssertionPortPropOutput: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionPortPropOutput)
    AssertionPortRef: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionPortRef)
    AssertionPortTypedLValue: typing.ClassVar[DiagCode]  # value = DiagCode(AssertionPortTypedLValue)
    AssignToCHandle: typing.ClassVar[DiagCode]  # value = DiagCode(AssignToCHandle)
    AssignToNet: typing.ClassVar[DiagCode]  # value = DiagCode(AssignToNet)
    AssignedToLocalBodyParam: typing.ClassVar[DiagCode]  # value = DiagCode(AssignedToLocalBodyParam)
    AssignedToLocalPortParam: typing.ClassVar[DiagCode]  # value = DiagCode(AssignedToLocalPortParam)
    AssignmentNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentNotAllowed)
    AssignmentPatternAssociativeType: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentPatternAssociativeType)
    AssignmentPatternDynamicDefault: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentPatternDynamicDefault)
    AssignmentPatternDynamicType: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentPatternDynamicType)
    AssignmentPatternKeyDupDefault: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentPatternKeyDupDefault)
    AssignmentPatternKeyDupName: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentPatternKeyDupName)
    AssignmentPatternKeyDupValue: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentPatternKeyDupValue)
    AssignmentPatternKeyExpr: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentPatternKeyExpr)
    AssignmentPatternLValueDynamic: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentPatternLValueDynamic)
    AssignmentPatternMissingElements: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentPatternMissingElements)
    AssignmentPatternNoContext: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentPatternNoContext)
    AssignmentPatternNoMember: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentPatternNoMember)
    AssignmentRequiresParens: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentRequiresParens)
    AssignmentToConstVar: typing.ClassVar[DiagCode]  # value = DiagCode(AssignmentToConstVar)
    AssociativeWildcardNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(AssociativeWildcardNotAllowed)
    AttributesNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(AttributesNotAllowed)
    AutoFromNonBlockingTiming: typing.ClassVar[DiagCode]  # value = DiagCode(AutoFromNonBlockingTiming)
    AutoFromNonProcedural: typing.ClassVar[DiagCode]  # value = DiagCode(AutoFromNonProcedural)
    AutoFromStaticInit: typing.ClassVar[DiagCode]  # value = DiagCode(AutoFromStaticInit)
    AutoVarToRefStatic: typing.ClassVar[DiagCode]  # value = DiagCode(AutoVarToRefStatic)
    AutoVarTraced: typing.ClassVar[DiagCode]  # value = DiagCode(AutoVarTraced)
    AutoVariableHierarchical: typing.ClassVar[DiagCode]  # value = DiagCode(AutoVariableHierarchical)
    AutomaticNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(AutomaticNotAllowed)
    BadAssignment: typing.ClassVar[DiagCode]  # value = DiagCode(BadAssignment)
    BadAssignmentPatternType: typing.ClassVar[DiagCode]  # value = DiagCode(BadAssignmentPatternType)
    BadBinaryDigit: typing.ClassVar[DiagCode]  # value = DiagCode(BadBinaryDigit)
    BadBinaryExpression: typing.ClassVar[DiagCode]  # value = DiagCode(BadBinaryExpression)
    BadCastType: typing.ClassVar[DiagCode]  # value = DiagCode(BadCastType)
    BadConcatExpression: typing.ClassVar[DiagCode]  # value = DiagCode(BadConcatExpression)
    BadConditionalExpression: typing.ClassVar[DiagCode]  # value = DiagCode(BadConditionalExpression)
    BadConversion: typing.ClassVar[DiagCode]  # value = DiagCode(BadConversion)
    BadDecimalDigit: typing.ClassVar[DiagCode]  # value = DiagCode(BadDecimalDigit)
    BadDisableSoft: typing.ClassVar[DiagCode]  # value = DiagCode(BadDisableSoft)
    BadFinishNum: typing.ClassVar[DiagCode]  # value = DiagCode(BadFinishNum)
    BadForceNetType: typing.ClassVar[DiagCode]  # value = DiagCode(BadForceNetType)
    BadHexDigit: typing.ClassVar[DiagCode]  # value = DiagCode(BadHexDigit)
    BadIndexExpression: typing.ClassVar[DiagCode]  # value = DiagCode(BadIndexExpression)
    BadInstanceArrayRange: typing.ClassVar[DiagCode]  # value = DiagCode(BadInstanceArrayRange)
    BadIntegerCast: typing.ClassVar[DiagCode]  # value = DiagCode(BadIntegerCast)
    BadOctalDigit: typing.ClassVar[DiagCode]  # value = DiagCode(BadOctalDigit)
    BadProceduralAssign: typing.ClassVar[DiagCode]  # value = DiagCode(BadProceduralAssign)
    BadProceduralForce: typing.ClassVar[DiagCode]  # value = DiagCode(BadProceduralForce)
    BadReplicationExpression: typing.ClassVar[DiagCode]  # value = DiagCode(BadReplicationExpression)
    BadSetMembershipType: typing.ClassVar[DiagCode]  # value = DiagCode(BadSetMembershipType)
    BadSliceType: typing.ClassVar[DiagCode]  # value = DiagCode(BadSliceType)
    BadSolveBefore: typing.ClassVar[DiagCode]  # value = DiagCode(BadSolveBefore)
    BadStreamCast: typing.ClassVar[DiagCode]  # value = DiagCode(BadStreamCast)
    BadStreamContext: typing.ClassVar[DiagCode]  # value = DiagCode(BadStreamContext)
    BadStreamExprType: typing.ClassVar[DiagCode]  # value = DiagCode(BadStreamExprType)
    BadStreamSize: typing.ClassVar[DiagCode]  # value = DiagCode(BadStreamSize)
    BadStreamSlice: typing.ClassVar[DiagCode]  # value = DiagCode(BadStreamSlice)
    BadStreamSourceType: typing.ClassVar[DiagCode]  # value = DiagCode(BadStreamSourceType)
    BadStreamTargetType: typing.ClassVar[DiagCode]  # value = DiagCode(BadStreamTargetType)
    BadStreamWithOrder: typing.ClassVar[DiagCode]  # value = DiagCode(BadStreamWithOrder)
    BadStreamWithType: typing.ClassVar[DiagCode]  # value = DiagCode(BadStreamWithType)
    BadSystemSubroutineArg: typing.ClassVar[DiagCode]  # value = DiagCode(BadSystemSubroutineArg)
    BadTypeParamExpr: typing.ClassVar[DiagCode]  # value = DiagCode(BadTypeParamExpr)
    BadUnaryExpression: typing.ClassVar[DiagCode]  # value = DiagCode(BadUnaryExpression)
    BadUniquenessType: typing.ClassVar[DiagCode]  # value = DiagCode(BadUniquenessType)
    BadValueRange: typing.ClassVar[DiagCode]  # value = DiagCode(BadValueRange)
    BaseConstructorDuplicate: typing.ClassVar[DiagCode]  # value = DiagCode(BaseConstructorDuplicate)
    BaseConstructorNotCalled: typing.ClassVar[DiagCode]  # value = DiagCode(BaseConstructorNotCalled)
    BiDiSwitchNetTypes: typing.ClassVar[DiagCode]  # value = DiagCode(BiDiSwitchNetTypes)
    BindDirectiveInvalidName: typing.ClassVar[DiagCode]  # value = DiagCode(BindDirectiveInvalidName)
    BindTargetPrimitive: typing.ClassVar[DiagCode]  # value = DiagCode(BindTargetPrimitive)
    BindTypeParamMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(BindTypeParamMismatch)
    BindTypeParamNotFound: typing.ClassVar[DiagCode]  # value = DiagCode(BindTypeParamNotFound)
    BindUnderBind: typing.ClassVar[DiagCode]  # value = DiagCode(BindUnderBind)
    BitwiseOpMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(BitwiseOpMismatch)
    BitwiseOpParentheses: typing.ClassVar[DiagCode]  # value = DiagCode(BitwiseOpParentheses)
    BitwiseRelPrecedence: typing.ClassVar[DiagCode]  # value = DiagCode(BitwiseRelPrecedence)
    BlockingAssignToFreeVar: typing.ClassVar[DiagCode]  # value = DiagCode(BlockingAssignToFreeVar)
    BlockingInAlwaysFF: typing.ClassVar[DiagCode]  # value = DiagCode(BlockingInAlwaysFF)
    BodyForPure: typing.ClassVar[DiagCode]  # value = DiagCode(BodyForPure)
    BodyForPureConstraint: typing.ClassVar[DiagCode]  # value = DiagCode(BodyForPureConstraint)
    BodyParamNoInitializer: typing.ClassVar[DiagCode]  # value = DiagCode(BodyParamNoInitializer)
    CHandleInAssertion: typing.ClassVar[DiagCode]  # value = DiagCode(CHandleInAssertion)
    CannotCompareTwoInstances: typing.ClassVar[DiagCode]  # value = DiagCode(CannotCompareTwoInstances)
    CannotDeclareType: typing.ClassVar[DiagCode]  # value = DiagCode(CannotDeclareType)
    CannotIndexScalar: typing.ClassVar[DiagCode]  # value = DiagCode(CannotIndexScalar)
    CantDeclarePortSigned: typing.ClassVar[DiagCode]  # value = DiagCode(CantDeclarePortSigned)
    CantModifyConst: typing.ClassVar[DiagCode]  # value = DiagCode(CantModifyConst)
    CaseDefault: typing.ClassVar[DiagCode]  # value = DiagCode(CaseDefault)
    CaseDup: typing.ClassVar[DiagCode]  # value = DiagCode(CaseDup)
    CaseEnum: typing.ClassVar[DiagCode]  # value = DiagCode(CaseEnum)
    CaseEnumExplicit: typing.ClassVar[DiagCode]  # value = DiagCode(CaseEnumExplicit)
    CaseGenerateDup: typing.ClassVar[DiagCode]  # value = DiagCode(CaseGenerateDup)
    CaseGenerateEmpty: typing.ClassVar[DiagCode]  # value = DiagCode(CaseGenerateEmpty)
    CaseGenerateNoBlock: typing.ClassVar[DiagCode]  # value = DiagCode(CaseGenerateNoBlock)
    CaseInsideKeyword: typing.ClassVar[DiagCode]  # value = DiagCode(CaseInsideKeyword)
    CaseNotWildcard: typing.ClassVar[DiagCode]  # value = DiagCode(CaseNotWildcard)
    CaseOutsideRange: typing.ClassVar[DiagCode]  # value = DiagCode(CaseOutsideRange)
    CaseOverlap: typing.ClassVar[DiagCode]  # value = DiagCode(CaseOverlap)
    CaseStatementEmpty: typing.ClassVar[DiagCode]  # value = DiagCode(CaseStatementEmpty)
    CaseTypeMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(CaseTypeMismatch)
    CaseZWithX: typing.ClassVar[DiagCode]  # value = DiagCode(CaseZWithX)
    ChainedMethodParens: typing.ClassVar[DiagCode]  # value = DiagCode(ChainedMethodParens)
    ChargeWithTriReg: typing.ClassVar[DiagCode]  # value = DiagCode(ChargeWithTriReg)
    CheckerArgCannotBeEmpty: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerArgCannotBeEmpty)
    CheckerBlockingAssign: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerBlockingAssign)
    CheckerClassBadInstantiation: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerClassBadInstantiation)
    CheckerFuncArg: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerFuncArg)
    CheckerFuncBadInstantiation: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerFuncBadInstantiation)
    CheckerHierarchical: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerHierarchical)
    CheckerInCheckerProc: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerInCheckerProc)
    CheckerInForkJoin: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerInForkJoin)
    CheckerOutputBadType: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerOutputBadType)
    CheckerParameterAssign: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerParameterAssign)
    CheckerPortDirectionType: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerPortDirectionType)
    CheckerPortInout: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerPortInout)
    CheckerTimingControl: typing.ClassVar[DiagCode]  # value = DiagCode(CheckerTimingControl)
    ClassInheritanceCycle: typing.ClassVar[DiagCode]  # value = DiagCode(ClassInheritanceCycle)
    ClassMemberInAssertion: typing.ClassVar[DiagCode]  # value = DiagCode(ClassMemberInAssertion)
    ClassPrivateMembersBitstream: typing.ClassVar[DiagCode]  # value = DiagCode(ClassPrivateMembersBitstream)
    ClassSpecifierConflict: typing.ClassVar[DiagCode]  # value = DiagCode(ClassSpecifierConflict)
    ClockVarAssignConcat: typing.ClassVar[DiagCode]  # value = DiagCode(ClockVarAssignConcat)
    ClockVarBadTiming: typing.ClassVar[DiagCode]  # value = DiagCode(ClockVarBadTiming)
    ClockVarOutputRead: typing.ClassVar[DiagCode]  # value = DiagCode(ClockVarOutputRead)
    ClockVarSyncDrive: typing.ClassVar[DiagCode]  # value = DiagCode(ClockVarSyncDrive)
    ClockVarTargetAssign: typing.ClassVar[DiagCode]  # value = DiagCode(ClockVarTargetAssign)
    ClockingBlockEventEdge: typing.ClassVar[DiagCode]  # value = DiagCode(ClockingBlockEventEdge)
    ClockingNameEmpty: typing.ClassVar[DiagCode]  # value = DiagCode(ClockingNameEmpty)
    ComparisonMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(ComparisonMismatch)
    CompilationUnitFromPackage: typing.ClassVar[DiagCode]  # value = DiagCode(CompilationUnitFromPackage)
    ConcatWithStringInt: typing.ClassVar[DiagCode]  # value = DiagCode(ConcatWithStringInt)
    ConcurrentAssertActionBlock: typing.ClassVar[DiagCode]  # value = DiagCode(ConcurrentAssertActionBlock)
    ConditionalPrecedence: typing.ClassVar[DiagCode]  # value = DiagCode(ConditionalPrecedence)
    ConfigDupTop: typing.ClassVar[DiagCode]  # value = DiagCode(ConfigDupTop)
    ConfigInstanceUnderOtherConfig: typing.ClassVar[DiagCode]  # value = DiagCode(ConfigInstanceUnderOtherConfig)
    ConfigInstanceWrongTop: typing.ClassVar[DiagCode]  # value = DiagCode(ConfigInstanceWrongTop)
    ConfigMissingName: typing.ClassVar[DiagCode]  # value = DiagCode(ConfigMissingName)
    ConfigOverrideTop: typing.ClassVar[DiagCode]  # value = DiagCode(ConfigOverrideTop)
    ConfigParamLiteral: typing.ClassVar[DiagCode]  # value = DiagCode(ConfigParamLiteral)
    ConfigParamsForPrimitive: typing.ClassVar[DiagCode]  # value = DiagCode(ConfigParamsForPrimitive)
    ConfigParamsIgnored: typing.ClassVar[DiagCode]  # value = DiagCode(ConfigParamsIgnored)
    ConfigParamsOrdered: typing.ClassVar[DiagCode]  # value = DiagCode(ConfigParamsOrdered)
    ConfigSpecificCellLiblist: typing.ClassVar[DiagCode]  # value = DiagCode(ConfigSpecificCellLiblist)
    ConsecutiveComparison: typing.ClassVar[DiagCode]  # value = DiagCode(ConsecutiveComparison)
    ConstEvalAssertionFailed: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalAssertionFailed)
    ConstEvalAssociativeElementNotFound: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalAssociativeElementNotFound)
    ConstEvalAssociativeIndexInvalid: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalAssociativeIndexInvalid)
    ConstEvalBitstreamCastSize: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalBitstreamCastSize)
    ConstEvalCaseItemsNotUnique: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalCaseItemsNotUnique)
    ConstEvalCheckers: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalCheckers)
    ConstEvalClassType: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalClassType)
    ConstEvalCovergroupType: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalCovergroupType)
    ConstEvalDPINotConstant: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalDPINotConstant)
    ConstEvalDisableTarget: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalDisableTarget)
    ConstEvalDynamicArrayIndex: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalDynamicArrayIndex)
    ConstEvalDynamicArrayRange: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalDynamicArrayRange)
    ConstEvalDynamicToFixedSize: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalDynamicToFixedSize)
    ConstEvalEmptyQueue: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalEmptyQueue)
    ConstEvalExceededMaxCallDepth: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalExceededMaxCallDepth)
    ConstEvalExceededMaxSteps: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalExceededMaxSteps)
    ConstEvalFunctionArgDirection: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalFunctionArgDirection)
    ConstEvalFunctionIdentifiersMustBeLocal: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalFunctionIdentifiersMustBeLocal)
    ConstEvalFunctionInsideGenerate: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalFunctionInsideGenerate)
    ConstEvalHierarchicalName: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalHierarchicalName)
    ConstEvalIdUsedInCEBeforeDecl: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalIdUsedInCEBeforeDecl)
    ConstEvalIfItemsNotUnique: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalIfItemsNotUnique)
    ConstEvalMethodNotConstant: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalMethodNotConstant)
    ConstEvalNoCaseItemsMatched: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalNoCaseItemsMatched)
    ConstEvalNoIfItemsMatched: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalNoIfItemsMatched)
    ConstEvalNonConstVariable: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalNonConstVariable)
    ConstEvalParallelBlockNotConst: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalParallelBlockNotConst)
    ConstEvalParamCycle: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalParamCycle)
    ConstEvalProceduralAssign: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalProceduralAssign)
    ConstEvalQueueRange: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalQueueRange)
    ConstEvalRandValue: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalRandValue)
    ConstEvalReplicationCountInvalid: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalReplicationCountInvalid)
    ConstEvalStaticSkipped: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalStaticSkipped)
    ConstEvalSubroutineNotConstant: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalSubroutineNotConstant)
    ConstEvalTaggedUnion: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalTaggedUnion)
    ConstEvalTaskNotConstant: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalTaskNotConstant)
    ConstEvalTimedStmtNotConst: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalTimedStmtNotConst)
    ConstEvalVoidNotConstant: typing.ClassVar[DiagCode]  # value = DiagCode(ConstEvalVoidNotConstant)
    ConstFunctionPortRequiresRef: typing.ClassVar[DiagCode]  # value = DiagCode(ConstFunctionPortRequiresRef)
    ConstPortNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(ConstPortNotAllowed)
    ConstSysTaskIgnored: typing.ClassVar[DiagCode]  # value = DiagCode(ConstSysTaskIgnored)
    ConstVarNoInitializer: typing.ClassVar[DiagCode]  # value = DiagCode(ConstVarNoInitializer)
    ConstVarToRef: typing.ClassVar[DiagCode]  # value = DiagCode(ConstVarToRef)
    ConstantConversion: typing.ClassVar[DiagCode]  # value = DiagCode(ConstantConversion)
    ConstraintNotInClass: typing.ClassVar[DiagCode]  # value = DiagCode(ConstraintNotInClass)
    ConstraintQualOutOfBlock: typing.ClassVar[DiagCode]  # value = DiagCode(ConstraintQualOutOfBlock)
    ConstructorOutsideClass: typing.ClassVar[DiagCode]  # value = DiagCode(ConstructorOutsideClass)
    ConstructorReturnType: typing.ClassVar[DiagCode]  # value = DiagCode(ConstructorReturnType)
    CopyClassTarget: typing.ClassVar[DiagCode]  # value = DiagCode(CopyClassTarget)
    CouldNotOpenIncludeFile: typing.ClassVar[DiagCode]  # value = DiagCode(CouldNotOpenIncludeFile)
    CouldNotResolveHierarchicalPath: typing.ClassVar[DiagCode]  # value = DiagCode(CouldNotResolveHierarchicalPath)
    CoverCrossItems: typing.ClassVar[DiagCode]  # value = DiagCode(CoverCrossItems)
    CoverOptionImmutable: typing.ClassVar[DiagCode]  # value = DiagCode(CoverOptionImmutable)
    CoverStmtNoFail: typing.ClassVar[DiagCode]  # value = DiagCode(CoverStmtNoFail)
    CoverageBinDefSeqSize: typing.ClassVar[DiagCode]  # value = DiagCode(CoverageBinDefSeqSize)
    CoverageBinDefaultIgnore: typing.ClassVar[DiagCode]  # value = DiagCode(CoverageBinDefaultIgnore)
    CoverageBinDefaultWildcard: typing.ClassVar[DiagCode]  # value = DiagCode(CoverageBinDefaultWildcard)
    CoverageBinTargetName: typing.ClassVar[DiagCode]  # value = DiagCode(CoverageBinTargetName)
    CoverageBinTransSize: typing.ClassVar[DiagCode]  # value = DiagCode(CoverageBinTransSize)
    CoverageExprVar: typing.ClassVar[DiagCode]  # value = DiagCode(CoverageExprVar)
    CoverageOptionDup: typing.ClassVar[DiagCode]  # value = DiagCode(CoverageOptionDup)
    CoverageSampleFormal: typing.ClassVar[DiagCode]  # value = DiagCode(CoverageSampleFormal)
    CoverageSetType: typing.ClassVar[DiagCode]  # value = DiagCode(CoverageSetType)
    CovergroupOutArg: typing.ClassVar[DiagCode]  # value = DiagCode(CovergroupOutArg)
    CycleDelayNonClock: typing.ClassVar[DiagCode]  # value = DiagCode(CycleDelayNonClock)
    DPIExportDifferentScope: typing.ClassVar[DiagCode]  # value = DiagCode(DPIExportDifferentScope)
    DPIExportDuplicate: typing.ClassVar[DiagCode]  # value = DiagCode(DPIExportDuplicate)
    DPIExportDuplicateCId: typing.ClassVar[DiagCode]  # value = DiagCode(DPIExportDuplicateCId)
    DPIExportImportedFunc: typing.ClassVar[DiagCode]  # value = DiagCode(DPIExportImportedFunc)
    DPIExportKindMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(DPIExportKindMismatch)
    DPIPureArg: typing.ClassVar[DiagCode]  # value = DiagCode(DPIPureArg)
    DPIPureReturn: typing.ClassVar[DiagCode]  # value = DiagCode(DPIPureReturn)
    DPIPureTask: typing.ClassVar[DiagCode]  # value = DiagCode(DPIPureTask)
    DPIRefArg: typing.ClassVar[DiagCode]  # value = DiagCode(DPIRefArg)
    DPISignatureMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(DPISignatureMismatch)
    DPISpecDisallowed: typing.ClassVar[DiagCode]  # value = DiagCode(DPISpecDisallowed)
    DecimalDigitMultipleUnknown: typing.ClassVar[DiagCode]  # value = DiagCode(DecimalDigitMultipleUnknown)
    DeclModifierConflict: typing.ClassVar[DiagCode]  # value = DiagCode(DeclModifierConflict)
    DeclModifierOrdering: typing.ClassVar[DiagCode]  # value = DiagCode(DeclModifierOrdering)
    DeclarationsAtStart: typing.ClassVar[DiagCode]  # value = DiagCode(DeclarationsAtStart)
    DefParamCycle: typing.ClassVar[DiagCode]  # value = DiagCode(DefParamCycle)
    DefParamLocal: typing.ClassVar[DiagCode]  # value = DiagCode(DefParamLocal)
    DefParamTarget: typing.ClassVar[DiagCode]  # value = DiagCode(DefParamTarget)
    DefParamTargetChange: typing.ClassVar[DiagCode]  # value = DiagCode(DefParamTargetChange)
    DefaultArgNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(DefaultArgNotAllowed)
    DefaultSuperArgLocalReference: typing.ClassVar[DiagCode]  # value = DiagCode(DefaultSuperArgLocalReference)
    DeferredAssertAutoRefArg: typing.ClassVar[DiagCode]  # value = DiagCode(DeferredAssertAutoRefArg)
    DeferredAssertNonVoid: typing.ClassVar[DiagCode]  # value = DiagCode(DeferredAssertNonVoid)
    DeferredAssertOutArg: typing.ClassVar[DiagCode]  # value = DiagCode(DeferredAssertOutArg)
    DeferredDelayMustBeZero: typing.ClassVar[DiagCode]  # value = DiagCode(DeferredDelayMustBeZero)
    DefinitionUsedAsType: typing.ClassVar[DiagCode]  # value = DiagCode(DefinitionUsedAsType)
    DefinitionUsedAsValue: typing.ClassVar[DiagCode]  # value = DiagCode(DefinitionUsedAsValue)
    DefparamBadHierarchy: typing.ClassVar[DiagCode]  # value = DiagCode(DefparamBadHierarchy)
    Delay3NotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(Delay3NotAllowed)
    Delay3OnVar: typing.ClassVar[DiagCode]  # value = DiagCode(Delay3OnVar)
    Delay3UdpNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(Delay3UdpNotAllowed)
    DelayNotNumeric: typing.ClassVar[DiagCode]  # value = DiagCode(DelayNotNumeric)
    DelaysNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(DelaysNotAllowed)
    DerivedCovergroupNoBase: typing.ClassVar[DiagCode]  # value = DiagCode(DerivedCovergroupNoBase)
    DerivedCovergroupNotInClass: typing.ClassVar[DiagCode]  # value = DiagCode(DerivedCovergroupNotInClass)
    DigitsLeadingUnderscore: typing.ClassVar[DiagCode]  # value = DiagCode(DigitsLeadingUnderscore)
    DimensionIndexInvalid: typing.ClassVar[DiagCode]  # value = DiagCode(DimensionIndexInvalid)
    DimensionRequiresConstRange: typing.ClassVar[DiagCode]  # value = DiagCode(DimensionRequiresConstRange)
    DirectionOnInterfacePort: typing.ClassVar[DiagCode]  # value = DiagCode(DirectionOnInterfacePort)
    DirectionWithInterfacePort: typing.ClassVar[DiagCode]  # value = DiagCode(DirectionWithInterfacePort)
    DirectiveInsideDesignElement: typing.ClassVar[DiagCode]  # value = DiagCode(DirectiveInsideDesignElement)
    DisableIffLocalVar: typing.ClassVar[DiagCode]  # value = DiagCode(DisableIffLocalVar)
    DisableIffMatched: typing.ClassVar[DiagCode]  # value = DiagCode(DisableIffMatched)
    DisallowedPortDefault: typing.ClassVar[DiagCode]  # value = DiagCode(DisallowedPortDefault)
    DistRealRangeWeight: typing.ClassVar[DiagCode]  # value = DiagCode(DistRealRangeWeight)
    DotIntoInstArray: typing.ClassVar[DiagCode]  # value = DiagCode(DotIntoInstArray)
    DotOnType: typing.ClassVar[DiagCode]  # value = DiagCode(DotOnType)
    DriveStrengthHighZ: typing.ClassVar[DiagCode]  # value = DiagCode(DriveStrengthHighZ)
    DriveStrengthInvalid: typing.ClassVar[DiagCode]  # value = DiagCode(DriveStrengthInvalid)
    DriveStrengthNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(DriveStrengthNotAllowed)
    DupConfigRule: typing.ClassVar[DiagCode]  # value = DiagCode(DupConfigRule)
    DupInterfaceExternMethod: typing.ClassVar[DiagCode]  # value = DiagCode(DupInterfaceExternMethod)
    DupTimingPath: typing.ClassVar[DiagCode]  # value = DiagCode(DupTimingPath)
    DuplicateArgAssignment: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicateArgAssignment)
    DuplicateAttribute: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicateAttribute)
    DuplicateBind: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicateBind)
    DuplicateClassSpecifier: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicateClassSpecifier)
    DuplicateDeclModifier: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicateDeclModifier)
    DuplicateDefinition: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicateDefinition)
    DuplicateDefparam: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicateDefparam)
    DuplicateImport: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicateImport)
    DuplicateParamAssignment: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicateParamAssignment)
    DuplicatePortConnection: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicatePortConnection)
    DuplicateQualifier: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicateQualifier)
    DuplicateWildcardPortConnection: typing.ClassVar[DiagCode]  # value = DiagCode(DuplicateWildcardPortConnection)
    DynamicDimensionIndex: typing.ClassVar[DiagCode]  # value = DiagCode(DynamicDimensionIndex)
    DynamicNotProcedural: typing.ClassVar[DiagCode]  # value = DiagCode(DynamicNotProcedural)
    EdgeDescWrongKeyword: typing.ClassVar[DiagCode]  # value = DiagCode(EdgeDescWrongKeyword)
    EmbeddedNull: typing.ClassVar[DiagCode]  # value = DiagCode(EmbeddedNull)
    EmptyArgNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(EmptyArgNotAllowed)
    EmptyAssignmentPattern: typing.ClassVar[DiagCode]  # value = DiagCode(EmptyAssignmentPattern)
    EmptyBody: typing.ClassVar[DiagCode]  # value = DiagCode(EmptyBody)
    EmptyConcatNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(EmptyConcatNotAllowed)
    EmptyMember: typing.ClassVar[DiagCode]  # value = DiagCode(EmptyMember)
    EmptyStatement: typing.ClassVar[DiagCode]  # value = DiagCode(EmptyStatement)
    EmptyUdpPort: typing.ClassVar[DiagCode]  # value = DiagCode(EmptyUdpPort)
    EndNameMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(EndNameMismatch)
    EndNameNotEmpty: typing.ClassVar[DiagCode]  # value = DiagCode(EndNameNotEmpty)
    EnumIncrementUnknown: typing.ClassVar[DiagCode]  # value = DiagCode(EnumIncrementUnknown)
    EnumRangeLiteral: typing.ClassVar[DiagCode]  # value = DiagCode(EnumRangeLiteral)
    EnumRangeMultiDimensional: typing.ClassVar[DiagCode]  # value = DiagCode(EnumRangeMultiDimensional)
    EnumValueDuplicate: typing.ClassVar[DiagCode]  # value = DiagCode(EnumValueDuplicate)
    EnumValueOutOfRange: typing.ClassVar[DiagCode]  # value = DiagCode(EnumValueOutOfRange)
    EnumValueOverflow: typing.ClassVar[DiagCode]  # value = DiagCode(EnumValueOverflow)
    EnumValueSizeMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(EnumValueSizeMismatch)
    EnumValueUnknownBits: typing.ClassVar[DiagCode]  # value = DiagCode(EnumValueUnknownBits)
    ErrorTask: typing.ClassVar[DiagCode]  # value = DiagCode(ErrorTask)
    EscapedWhitespace: typing.ClassVar[DiagCode]  # value = DiagCode(EscapedWhitespace)
    EventExprAssertionArg: typing.ClassVar[DiagCode]  # value = DiagCode(EventExprAssertionArg)
    EventExpressionConstant: typing.ClassVar[DiagCode]  # value = DiagCode(EventExpressionConstant)
    EventExpressionFuncArg: typing.ClassVar[DiagCode]  # value = DiagCode(EventExpressionFuncArg)
    ExceededMaxIncludeDepth: typing.ClassVar[DiagCode]  # value = DiagCode(ExceededMaxIncludeDepth)
    ExpectedAnsiPort: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedAnsiPort)
    ExpectedArgument: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedArgument)
    ExpectedAssertionItemPort: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedAssertionItemPort)
    ExpectedAssignmentKey: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedAssignmentKey)
    ExpectedAttribute: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedAttribute)
    ExpectedCaseItem: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedCaseItem)
    ExpectedClassPropertyName: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedClassPropertyName)
    ExpectedClassSpecifier: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedClassSpecifier)
    ExpectedClockingSkew: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedClockingSkew)
    ExpectedClosingQuote: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedClosingQuote)
    ExpectedConditionalPattern: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedConditionalPattern)
    ExpectedConstraintName: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedConstraintName)
    ExpectedContinuousAssignment: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedContinuousAssignment)
    ExpectedDPISpecString: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedDPISpecString)
    ExpectedDeclarator: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedDeclarator)
    ExpectedDiagPragmaArg: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedDiagPragmaArg)
    ExpectedDiagPragmaLevel: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedDiagPragmaLevel)
    ExpectedDistItem: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedDistItem)
    ExpectedDriveStrength: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedDriveStrength)
    ExpectedEdgeDescriptor: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedEdgeDescriptor)
    ExpectedEnumBase: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedEnumBase)
    ExpectedExpression: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedExpression)
    ExpectedForInitializer: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedForInitializer)
    ExpectedFunctionPort: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedFunctionPort)
    ExpectedFunctionPortList: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedFunctionPortList)
    ExpectedGenvarIterVar: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedGenvarIterVar)
    ExpectedHierarchicalInstantiation: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedHierarchicalInstantiation)
    ExpectedIdentifier: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedIdentifier)
    ExpectedIfOrCase: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedIfOrCase)
    ExpectedImportExport: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedImportExport)
    ExpectedIncludeFileName: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedIncludeFileName)
    ExpectedIntegerBaseAfterSigned: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedIntegerBaseAfterSigned)
    ExpectedIntegerLiteral: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedIntegerLiteral)
    ExpectedInterfaceClassName: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedInterfaceClassName)
    ExpectedIterationExpression: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedIterationExpression)
    ExpectedIteratorName: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedIteratorName)
    ExpectedMacroArgs: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedMacroArgs)
    ExpectedMacroStringifyEnd: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedMacroStringifyEnd)
    ExpectedMember: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedMember)
    ExpectedModOrVarName: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedModOrVarName)
    ExpectedModportPort: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedModportPort)
    ExpectedModuleInstance: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedModuleInstance)
    ExpectedModuleName: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedModuleName)
    ExpectedNetDelay: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedNetDelay)
    ExpectedNetRef: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedNetRef)
    ExpectedNetStrength: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedNetStrength)
    ExpectedNetType: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedNetType)
    ExpectedNonAnsiPort: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedNonAnsiPort)
    ExpectedPackageImport: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedPackageImport)
    ExpectedParameterPort: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedParameterPort)
    ExpectedPathOp: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedPathOp)
    ExpectedPattern: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedPattern)
    ExpectedPortConnection: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedPortConnection)
    ExpectedPortList: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedPortList)
    ExpectedPragmaExpression: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedPragmaExpression)
    ExpectedPragmaName: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedPragmaName)
    ExpectedProtectArg: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedProtectArg)
    ExpectedProtectKeyword: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedProtectKeyword)
    ExpectedRsRule: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedRsRule)
    ExpectedSampleKeyword: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedSampleKeyword)
    ExpectedScopeName: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedScopeName)
    ExpectedScopeOrAssert: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedScopeOrAssert)
    ExpectedStatement: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedStatement)
    ExpectedStreamExpression: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedStreamExpression)
    ExpectedStringLiteral: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedStringLiteral)
    ExpectedSubroutineName: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedSubroutineName)
    ExpectedTimeLiteral: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedTimeLiteral)
    ExpectedToken: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedToken)
    ExpectedUdpPort: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedUdpPort)
    ExpectedUdpSymbol: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedUdpSymbol)
    ExpectedValueRangeElement: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedValueRangeElement)
    ExpectedVariableAssignment: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedVariableAssignment)
    ExpectedVariableName: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedVariableName)
    ExpectedVectorDigits: typing.ClassVar[DiagCode]  # value = DiagCode(ExpectedVectorDigits)
    ExprMustBeIntegral: typing.ClassVar[DiagCode]  # value = DiagCode(ExprMustBeIntegral)
    ExprNotConstraint: typing.ClassVar[DiagCode]  # value = DiagCode(ExprNotConstraint)
    ExprNotStatement: typing.ClassVar[DiagCode]  # value = DiagCode(ExprNotStatement)
    ExpressionNotAssignable: typing.ClassVar[DiagCode]  # value = DiagCode(ExpressionNotAssignable)
    ExpressionNotCallable: typing.ClassVar[DiagCode]  # value = DiagCode(ExpressionNotCallable)
    ExtendClassFromIface: typing.ClassVar[DiagCode]  # value = DiagCode(ExtendClassFromIface)
    ExtendFromFinal: typing.ClassVar[DiagCode]  # value = DiagCode(ExtendFromFinal)
    ExtendIfaceFromClass: typing.ClassVar[DiagCode]  # value = DiagCode(ExtendIfaceFromClass)
    ExternDeclMismatchImpl: typing.ClassVar[DiagCode]  # value = DiagCode(ExternDeclMismatchImpl)
    ExternDeclMismatchPrev: typing.ClassVar[DiagCode]  # value = DiagCode(ExternDeclMismatchPrev)
    ExternFuncForkJoin: typing.ClassVar[DiagCode]  # value = DiagCode(ExternFuncForkJoin)
    ExternIfaceArrayMethod: typing.ClassVar[DiagCode]  # value = DiagCode(ExternIfaceArrayMethod)
    ExternWildcardPortList: typing.ClassVar[DiagCode]  # value = DiagCode(ExternWildcardPortList)
    ExtraPragmaArgs: typing.ClassVar[DiagCode]  # value = DiagCode(ExtraPragmaArgs)
    ExtraProtectEnd: typing.ClassVar[DiagCode]  # value = DiagCode(ExtraProtectEnd)
    FatalTask: typing.ClassVar[DiagCode]  # value = DiagCode(FatalTask)
    FinalSpecifierLast: typing.ClassVar[DiagCode]  # value = DiagCode(FinalSpecifierLast)
    FinalWithPure: typing.ClassVar[DiagCode]  # value = DiagCode(FinalWithPure)
    FloatBoolConv: typing.ClassVar[DiagCode]  # value = DiagCode(FloatBoolConv)
    FloatIntConv: typing.ClassVar[DiagCode]  # value = DiagCode(FloatIntConv)
    FloatNarrow: typing.ClassVar[DiagCode]  # value = DiagCode(FloatNarrow)
    FloatWiden: typing.ClassVar[DiagCode]  # value = DiagCode(FloatWiden)
    ForeachDynamicDimAfterSkipped: typing.ClassVar[DiagCode]  # value = DiagCode(ForeachDynamicDimAfterSkipped)
    ForeachWildcardIndex: typing.ClassVar[DiagCode]  # value = DiagCode(ForeachWildcardIndex)
    ForkJoinAlwaysComb: typing.ClassVar[DiagCode]  # value = DiagCode(ForkJoinAlwaysComb)
    FormatEmptyArg: typing.ClassVar[DiagCode]  # value = DiagCode(FormatEmptyArg)
    FormatMismatchedType: typing.ClassVar[DiagCode]  # value = DiagCode(FormatMismatchedType)
    FormatMultibitStrength: typing.ClassVar[DiagCode]  # value = DiagCode(FormatMultibitStrength)
    FormatNoArgument: typing.ClassVar[DiagCode]  # value = DiagCode(FormatNoArgument)
    FormatRealInt: typing.ClassVar[DiagCode]  # value = DiagCode(FormatRealInt)
    FormatSpecifierInvalidWidth: typing.ClassVar[DiagCode]  # value = DiagCode(FormatSpecifierInvalidWidth)
    FormatSpecifierNotFloat: typing.ClassVar[DiagCode]  # value = DiagCode(FormatSpecifierNotFloat)
    FormatSpecifierWidthNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(FormatSpecifierWidthNotAllowed)
    FormatTooManyArgs: typing.ClassVar[DiagCode]  # value = DiagCode(FormatTooManyArgs)
    FormatUnspecifiedType: typing.ClassVar[DiagCode]  # value = DiagCode(FormatUnspecifiedType)
    ForwardTypedefDoesNotMatch: typing.ClassVar[DiagCode]  # value = DiagCode(ForwardTypedefDoesNotMatch)
    ForwardTypedefVisibility: typing.ClassVar[DiagCode]  # value = DiagCode(ForwardTypedefVisibility)
    GateUDNTConn: typing.ClassVar[DiagCode]  # value = DiagCode(GateUDNTConn)
    GenericClassScopeResolution: typing.ClassVar[DiagCode]  # value = DiagCode(GenericClassScopeResolution)
    GenvarDuplicate: typing.ClassVar[DiagCode]  # value = DiagCode(GenvarDuplicate)
    GenvarUnknownBits: typing.ClassVar[DiagCode]  # value = DiagCode(GenvarUnknownBits)
    GlobalClockEventExpr: typing.ClassVar[DiagCode]  # value = DiagCode(GlobalClockEventExpr)
    GlobalClockingEmpty: typing.ClassVar[DiagCode]  # value = DiagCode(GlobalClockingEmpty)
    GlobalClockingGenerate: typing.ClassVar[DiagCode]  # value = DiagCode(GlobalClockingGenerate)
    GlobalSampledValueAssertionExpr: typing.ClassVar[DiagCode]  # value = DiagCode(GlobalSampledValueAssertionExpr)
    GlobalSampledValueNested: typing.ClassVar[DiagCode]  # value = DiagCode(GlobalSampledValueNested)
    HierarchicalFromPackage: typing.ClassVar[DiagCode]  # value = DiagCode(HierarchicalFromPackage)
    IfNoneEdgeSensitive: typing.ClassVar[DiagCode]  # value = DiagCode(IfNoneEdgeSensitive)
    IfaceExtendIncomplete: typing.ClassVar[DiagCode]  # value = DiagCode(IfaceExtendIncomplete)
    IfaceExtendTypeParam: typing.ClassVar[DiagCode]  # value = DiagCode(IfaceExtendTypeParam)
    IfaceImportExportTarget: typing.ClassVar[DiagCode]  # value = DiagCode(IfaceImportExportTarget)
    IfaceMethodHidden: typing.ClassVar[DiagCode]  # value = DiagCode(IfaceMethodHidden)
    IfaceMethodNoImpl: typing.ClassVar[DiagCode]  # value = DiagCode(IfaceMethodNoImpl)
    IfaceMethodNotExtern: typing.ClassVar[DiagCode]  # value = DiagCode(IfaceMethodNotExtern)
    IfaceMethodNotVirtual: typing.ClassVar[DiagCode]  # value = DiagCode(IfaceMethodNotVirtual)
    IfaceMethodPure: typing.ClassVar[DiagCode]  # value = DiagCode(IfaceMethodPure)
    IfaceNameConflict: typing.ClassVar[DiagCode]  # value = DiagCode(IfaceNameConflict)
    IfacePortInExpr: typing.ClassVar[DiagCode]  # value = DiagCode(IfacePortInExpr)
    IgnoredMacroPaste: typing.ClassVar[DiagCode]  # value = DiagCode(IgnoredMacroPaste)
    IgnoredSlice: typing.ClassVar[DiagCode]  # value = DiagCode(IgnoredSlice)
    IllegalReferenceToProgramItem: typing.ClassVar[DiagCode]  # value = DiagCode(IllegalReferenceToProgramItem)
    ImplementNonIface: typing.ClassVar[DiagCode]  # value = DiagCode(ImplementNonIface)
    ImplicitConnNetInconsistent: typing.ClassVar[DiagCode]  # value = DiagCode(ImplicitConnNetInconsistent)
    ImplicitConvert: typing.ClassVar[DiagCode]  # value = DiagCode(ImplicitConvert)
    ImplicitNamedPortNotFound: typing.ClassVar[DiagCode]  # value = DiagCode(ImplicitNamedPortNotFound)
    ImplicitNamedPortTypeMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(ImplicitNamedPortTypeMismatch)
    ImplicitNetPortNoDefault: typing.ClassVar[DiagCode]  # value = DiagCode(ImplicitNetPortNoDefault)
    ImplicitNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(ImplicitNotAllowed)
    ImportNameCollision: typing.ClassVar[DiagCode]  # value = DiagCode(ImportNameCollision)
    InOutDefaultSkew: typing.ClassVar[DiagCode]  # value = DiagCode(InOutDefaultSkew)
    InOutPortCannotBeVariable: typing.ClassVar[DiagCode]  # value = DiagCode(InOutPortCannotBeVariable)
    InOutUWireConn: typing.ClassVar[DiagCode]  # value = DiagCode(InOutUWireConn)
    InOutUWirePort: typing.ClassVar[DiagCode]  # value = DiagCode(InOutUWirePort)
    InOutVarPortConn: typing.ClassVar[DiagCode]  # value = DiagCode(InOutVarPortConn)
    IncDecNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(IncDecNotAllowed)
    IndexOOB: typing.ClassVar[DiagCode]  # value = DiagCode(IndexOOB)
    IndexValueInvalid: typing.ClassVar[DiagCode]  # value = DiagCode(IndexValueInvalid)
    InequivalentUniquenessTypes: typing.ClassVar[DiagCode]  # value = DiagCode(InequivalentUniquenessTypes)
    InferredValDefArg: typing.ClassVar[DiagCode]  # value = DiagCode(InferredValDefArg)
    InfinitelyRecursiveHierarchy: typing.ClassVar[DiagCode]  # value = DiagCode(InfinitelyRecursiveHierarchy)
    InfoTask: typing.ClassVar[DiagCode]  # value = DiagCode(InfoTask)
    InheritFromAbstract: typing.ClassVar[DiagCode]  # value = DiagCode(InheritFromAbstract)
    InheritFromAbstractConstraint: typing.ClassVar[DiagCode]  # value = DiagCode(InheritFromAbstractConstraint)
    InitializerRequired: typing.ClassVar[DiagCode]  # value = DiagCode(InitializerRequired)
    InputPortAssign: typing.ClassVar[DiagCode]  # value = DiagCode(InputPortAssign)
    InputPortCoercion: typing.ClassVar[DiagCode]  # value = DiagCode(InputPortCoercion)
    InstanceArrayEndianMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(InstanceArrayEndianMismatch)
    InstanceMissingParens: typing.ClassVar[DiagCode]  # value = DiagCode(InstanceMissingParens)
    InstanceNameRequired: typing.ClassVar[DiagCode]  # value = DiagCode(InstanceNameRequired)
    InstanceWithDelay: typing.ClassVar[DiagCode]  # value = DiagCode(InstanceWithDelay)
    InstanceWithStrength: typing.ClassVar[DiagCode]  # value = DiagCode(InstanceWithStrength)
    IntBoolConv: typing.ClassVar[DiagCode]  # value = DiagCode(IntBoolConv)
    IntFloatConv: typing.ClassVar[DiagCode]  # value = DiagCode(IntFloatConv)
    InterconnectDelaySyntax: typing.ClassVar[DiagCode]  # value = DiagCode(InterconnectDelaySyntax)
    InterconnectInitializer: typing.ClassVar[DiagCode]  # value = DiagCode(InterconnectInitializer)
    InterconnectMultiPort: typing.ClassVar[DiagCode]  # value = DiagCode(InterconnectMultiPort)
    InterconnectPortVar: typing.ClassVar[DiagCode]  # value = DiagCode(InterconnectPortVar)
    InterconnectReference: typing.ClassVar[DiagCode]  # value = DiagCode(InterconnectReference)
    InterconnectTypeSyntax: typing.ClassVar[DiagCode]  # value = DiagCode(InterconnectTypeSyntax)
    InterfacePortInvalidExpression: typing.ClassVar[DiagCode]  # value = DiagCode(InterfacePortInvalidExpression)
    InterfacePortNotConnected: typing.ClassVar[DiagCode]  # value = DiagCode(InterfacePortNotConnected)
    InterfacePortTypeMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(InterfacePortTypeMismatch)
    InvalidAccessDotColon: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidAccessDotColon)
    InvalidArgumentExpr: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidArgumentExpr)
    InvalidArrayElemType: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidArrayElemType)
    InvalidArraySize: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidArraySize)
    InvalidAssociativeIndexType: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidAssociativeIndexType)
    InvalidBindTarget: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidBindTarget)
    InvalidBinsMatches: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidBinsMatches)
    InvalidBinsTarget: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidBinsTarget)
    InvalidBlockEventTarget: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidBlockEventTarget)
    InvalidClassAccess: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidClassAccess)
    InvalidClockingSignal: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidClockingSignal)
    InvalidCommaInPropExpr: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidCommaInPropExpr)
    InvalidConstraintExpr: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidConstraintExpr)
    InvalidConstraintQualifier: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidConstraintQualifier)
    InvalidConstructorAccess: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidConstructorAccess)
    InvalidCoverageExpr: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidCoverageExpr)
    InvalidCoverageOption: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidCoverageOption)
    InvalidDPIArgType: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidDPIArgType)
    InvalidDPICIdentifier: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidDPICIdentifier)
    InvalidDPIReturnType: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidDPIReturnType)
    InvalidDeferredAssertAction: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidDeferredAssertAction)
    InvalidDelayValue: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidDelayValue)
    InvalidDimensionRange: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidDimensionRange)
    InvalidDisableTarget: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidDisableTarget)
    InvalidDistExpression: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidDistExpression)
    InvalidEdgeDescriptor: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidEdgeDescriptor)
    InvalidEncodingByte: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidEncodingByte)
    InvalidEnumBase: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidEnumBase)
    InvalidEventExpression: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidEventExpression)
    InvalidExtendsDefault: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidExtendsDefault)
    InvalidForInitializer: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidForInitializer)
    InvalidForStepExpression: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidForStepExpression)
    InvalidGenvarIterExpression: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidGenvarIterExpression)
    InvalidHexEscapeCode: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidHexEscapeCode)
    InvalidHierarchicalIfacePortConn: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidHierarchicalIfacePortConn)
    InvalidInferredTimeScale: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidInferredTimeScale)
    InvalidInstanceForParent: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidInstanceForParent)
    InvalidLineDirectiveLevel: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidLineDirectiveLevel)
    InvalidMacroName: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidMacroName)
    InvalidMatchItem: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidMatchItem)
    InvalidMemberAccess: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidMemberAccess)
    InvalidMethodOverride: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidMethodOverride)
    InvalidMethodQualifier: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidMethodQualifier)
    InvalidModportAccess: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidModportAccess)
    InvalidNGateCount: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidNGateCount)
    InvalidNetType: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidNetType)
    InvalidPackageDecl: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPackageDecl)
    InvalidParamOverrideOpt: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidParamOverrideOpt)
    InvalidPortSubType: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPortSubType)
    InvalidPortType: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPortType)
    InvalidPragmaNumber: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPragmaNumber)
    InvalidPragmaViewport: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPragmaViewport)
    InvalidPrimInstanceForParent: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPrimInstanceForParent)
    InvalidPrimitivePortConn: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPrimitivePortConn)
    InvalidPropertyIndex: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPropertyIndex)
    InvalidPropertyQualifier: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPropertyQualifier)
    InvalidPropertyRange: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPropertyRange)
    InvalidPullStrength: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPullStrength)
    InvalidPulseStyle: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidPulseStyle)
    InvalidQualifierForConstructor: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidQualifierForConstructor)
    InvalidQualifierForIfaceMember: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidQualifierForIfaceMember)
    InvalidQualifierForMember: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidQualifierForMember)
    InvalidRandType: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidRandType)
    InvalidRandomizeOverride: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidRandomizeOverride)
    InvalidRefArg: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidRefArg)
    InvalidRepeatRange: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidRepeatRange)
    InvalidScopeIndexExpression: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidScopeIndexExpression)
    InvalidSelectExpression: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidSelectExpression)
    InvalidSignalEventInSeq: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidSignalEventInSeq)
    InvalidSpecifyDest: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidSpecifyDest)
    InvalidSpecifyPath: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidSpecifyPath)
    InvalidSpecifySource: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidSpecifySource)
    InvalidSpecifyType: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidSpecifyType)
    InvalidStmtInChecker: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidStmtInChecker)
    InvalidStringArg: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidStringArg)
    InvalidSuperNew: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidSuperNew)
    InvalidSuperNewDefault: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidSuperNewDefault)
    InvalidSyntaxInEventExpr: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidSyntaxInEventExpr)
    InvalidThisHandle: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidThisHandle)
    InvalidTimeScalePrecision: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidTimeScalePrecision)
    InvalidTimeScaleSpecifier: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidTimeScaleSpecifier)
    InvalidTimingCheckNotifierArg: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidTimingCheckNotifierArg)
    InvalidTopModule: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidTopModule)
    InvalidUTF8Seq: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidUTF8Seq)
    InvalidUnionMember: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidUnionMember)
    InvalidUniquenessExpr: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidUniquenessExpr)
    InvalidUserDefinedNetType: typing.ClassVar[DiagCode]  # value = DiagCode(InvalidUserDefinedNetType)
    IsUnboundedParamArg: typing.ClassVar[DiagCode]  # value = DiagCode(IsUnboundedParamArg)
    IteratorArgsWithoutWithClause: typing.ClassVar[DiagCode]  # value = DiagCode(IteratorArgsWithoutWithClause)
    LabelAndName: typing.ClassVar[DiagCode]  # value = DiagCode(LabelAndName)
    LetHierarchical: typing.ClassVar[DiagCode]  # value = DiagCode(LetHierarchical)
    LifetimeForPrototype: typing.ClassVar[DiagCode]  # value = DiagCode(LifetimeForPrototype)
    LiteralSizeIsZero: typing.ClassVar[DiagCode]  # value = DiagCode(LiteralSizeIsZero)
    LiteralSizeTooLarge: typing.ClassVar[DiagCode]  # value = DiagCode(LiteralSizeTooLarge)
    LocalFormalVarMultiAssign: typing.ClassVar[DiagCode]  # value = DiagCode(LocalFormalVarMultiAssign)
    LocalMemberAccess: typing.ClassVar[DiagCode]  # value = DiagCode(LocalMemberAccess)
    LocalNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(LocalNotAllowed)
    LocalParamNoInitializer: typing.ClassVar[DiagCode]  # value = DiagCode(LocalParamNoInitializer)
    LocalVarEventExpr: typing.ClassVar[DiagCode]  # value = DiagCode(LocalVarEventExpr)
    LocalVarMatchItem: typing.ClassVar[DiagCode]  # value = DiagCode(LocalVarMatchItem)
    LocalVarOutputEmptyMatch: typing.ClassVar[DiagCode]  # value = DiagCode(LocalVarOutputEmptyMatch)
    LocalVarTypeRequired: typing.ClassVar[DiagCode]  # value = DiagCode(LocalVarTypeRequired)
    LogicalNotParentheses: typing.ClassVar[DiagCode]  # value = DiagCode(LogicalNotParentheses)
    LogicalOpParentheses: typing.ClassVar[DiagCode]  # value = DiagCode(LogicalOpParentheses)
    LoopVarShadowsArray: typing.ClassVar[DiagCode]  # value = DiagCode(LoopVarShadowsArray)
    MacroOpsOutsideDefinition: typing.ClassVar[DiagCode]  # value = DiagCode(MacroOpsOutsideDefinition)
    MacroTokensAfterPragmaProtect: typing.ClassVar[DiagCode]  # value = DiagCode(MacroTokensAfterPragmaProtect)
    MatchItemsAdmitEmpty: typing.ClassVar[DiagCode]  # value = DiagCode(MatchItemsAdmitEmpty)
    MaxGenerateStepsExceeded: typing.ClassVar[DiagCode]  # value = DiagCode(MaxGenerateStepsExceeded)
    MaxInstanceArrayExceeded: typing.ClassVar[DiagCode]  # value = DiagCode(MaxInstanceArrayExceeded)
    MaxInstanceDepthExceeded: typing.ClassVar[DiagCode]  # value = DiagCode(MaxInstanceDepthExceeded)
    MemberDefinitionBeforeClass: typing.ClassVar[DiagCode]  # value = DiagCode(MemberDefinitionBeforeClass)
    MethodArgCountMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(MethodArgCountMismatch)
    MethodArgDefaultMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(MethodArgDefaultMismatch)
    MethodArgDirectionMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(MethodArgDirectionMismatch)
    MethodArgNameMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(MethodArgNameMismatch)
    MethodArgNoDefault: typing.ClassVar[DiagCode]  # value = DiagCode(MethodArgNoDefault)
    MethodArgTypeMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(MethodArgTypeMismatch)
    MethodKindMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(MethodKindMismatch)
    MethodReturnMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(MethodReturnMismatch)
    MethodReturnTypeScoped: typing.ClassVar[DiagCode]  # value = DiagCode(MethodReturnTypeScoped)
    MethodStaticLifetime: typing.ClassVar[DiagCode]  # value = DiagCode(MethodStaticLifetime)
    MismatchConstraintSpecifiers: typing.ClassVar[DiagCode]  # value = DiagCode(MismatchConstraintSpecifiers)
    MismatchStaticConstraint: typing.ClassVar[DiagCode]  # value = DiagCode(MismatchStaticConstraint)
    MismatchedEndKeywordsDirective: typing.ClassVar[DiagCode]  # value = DiagCode(MismatchedEndKeywordsDirective)
    MismatchedTimeScales: typing.ClassVar[DiagCode]  # value = DiagCode(MismatchedTimeScales)
    MismatchedUserDefPortConn: typing.ClassVar[DiagCode]  # value = DiagCode(MismatchedUserDefPortConn)
    MismatchedUserDefPortDir: typing.ClassVar[DiagCode]  # value = DiagCode(MismatchedUserDefPortDir)
    MisplacedDirectiveChar: typing.ClassVar[DiagCode]  # value = DiagCode(MisplacedDirectiveChar)
    MisplacedTrailingSeparator: typing.ClassVar[DiagCode]  # value = DiagCode(MisplacedTrailingSeparator)
    MissingConstraintBlock: typing.ClassVar[DiagCode]  # value = DiagCode(MissingConstraintBlock)
    MissingEndIfDirective: typing.ClassVar[DiagCode]  # value = DiagCode(MissingEndIfDirective)
    MissingExponentDigits: typing.ClassVar[DiagCode]  # value = DiagCode(MissingExponentDigits)
    MissingExportImpl: typing.ClassVar[DiagCode]  # value = DiagCode(MissingExportImpl)
    MissingExternImpl: typing.ClassVar[DiagCode]  # value = DiagCode(MissingExternImpl)
    MissingExternModuleImpl: typing.ClassVar[DiagCode]  # value = DiagCode(MissingExternModuleImpl)
    MissingExternWildcardPorts: typing.ClassVar[DiagCode]  # value = DiagCode(MissingExternWildcardPorts)
    MissingFormatSpecifier: typing.ClassVar[DiagCode]  # value = DiagCode(MissingFormatSpecifier)
    MissingFractionalDigits: typing.ClassVar[DiagCode]  # value = DiagCode(MissingFractionalDigits)
    MissingInvocationParens: typing.ClassVar[DiagCode]  # value = DiagCode(MissingInvocationParens)
    MissingModportPortDirection: typing.ClassVar[DiagCode]  # value = DiagCode(MissingModportPortDirection)
    MissingPortIODeclaration: typing.ClassVar[DiagCode]  # value = DiagCode(MissingPortIODeclaration)
    MissingReturnValue: typing.ClassVar[DiagCode]  # value = DiagCode(MissingReturnValue)
    MissingReturnValueProd: typing.ClassVar[DiagCode]  # value = DiagCode(MissingReturnValueProd)
    MissingTimeScale: typing.ClassVar[DiagCode]  # value = DiagCode(MissingTimeScale)
    MixedVarAssigns: typing.ClassVar[DiagCode]  # value = DiagCode(MixedVarAssigns)
    MixingOrderedAndNamedArgs: typing.ClassVar[DiagCode]  # value = DiagCode(MixingOrderedAndNamedArgs)
    MixingOrderedAndNamedParams: typing.ClassVar[DiagCode]  # value = DiagCode(MixingOrderedAndNamedParams)
    MixingOrderedAndNamedPorts: typing.ClassVar[DiagCode]  # value = DiagCode(MixingOrderedAndNamedPorts)
    MixingSubroutinePortKinds: typing.ClassVar[DiagCode]  # value = DiagCode(MixingSubroutinePortKinds)
    ModportConnMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(ModportConnMismatch)
    MultiBitEdge: typing.ClassVar[DiagCode]  # value = DiagCode(MultiBitEdge)
    MultipleAlwaysAssigns: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleAlwaysAssigns)
    MultipleContAssigns: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleContAssigns)
    MultipleDefaultCases: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleDefaultCases)
    MultipleDefaultClocking: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleDefaultClocking)
    MultipleDefaultConstructorArg: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleDefaultConstructorArg)
    MultipleDefaultDisable: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleDefaultDisable)
    MultipleDefaultDistWeight: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleDefaultDistWeight)
    MultipleDefaultInputSkew: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleDefaultInputSkew)
    MultipleDefaultOutputSkew: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleDefaultOutputSkew)
    MultipleDefaultRules: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleDefaultRules)
    MultipleGenerateDefaultCases: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleGenerateDefaultCases)
    MultipleGlobalClocking: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleGlobalClocking)
    MultipleNetAlias: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleNetAlias)
    MultiplePackedOpenArrays: typing.ClassVar[DiagCode]  # value = DiagCode(MultiplePackedOpenArrays)
    MultipleParallelTerminals: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleParallelTerminals)
    MultipleTopDupName: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleTopDupName)
    MultipleUDNTDrivers: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleUDNTDrivers)
    MultipleUWireDrivers: typing.ClassVar[DiagCode]  # value = DiagCode(MultipleUWireDrivers)
    NTResolveArgModify: typing.ClassVar[DiagCode]  # value = DiagCode(NTResolveArgModify)
    NTResolveClass: typing.ClassVar[DiagCode]  # value = DiagCode(NTResolveClass)
    NTResolveReturn: typing.ClassVar[DiagCode]  # value = DiagCode(NTResolveReturn)
    NTResolveSingleArg: typing.ClassVar[DiagCode]  # value = DiagCode(NTResolveSingleArg)
    NTResolveTask: typing.ClassVar[DiagCode]  # value = DiagCode(NTResolveTask)
    NTResolveUserDef: typing.ClassVar[DiagCode]  # value = DiagCode(NTResolveUserDef)
    NameListWithScopeRandomize: typing.ClassVar[DiagCode]  # value = DiagCode(NameListWithScopeRandomize)
    NamedArgNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(NamedArgNotAllowed)
    NegativeTimingLimit: typing.ClassVar[DiagCode]  # value = DiagCode(NegativeTimingLimit)
    NestedBlockComment: typing.ClassVar[DiagCode]  # value = DiagCode(NestedBlockComment)
    NestedConfigMultipleTops: typing.ClassVar[DiagCode]  # value = DiagCode(NestedConfigMultipleTops)
    NestedDisableIff: typing.ClassVar[DiagCode]  # value = DiagCode(NestedDisableIff)
    NestedIface: typing.ClassVar[DiagCode]  # value = DiagCode(NestedIface)
    NestedNonStaticClassMethod: typing.ClassVar[DiagCode]  # value = DiagCode(NestedNonStaticClassMethod)
    NestedNonStaticClassProperty: typing.ClassVar[DiagCode]  # value = DiagCode(NestedNonStaticClassProperty)
    NestedProtectBegin: typing.ClassVar[DiagCode]  # value = DiagCode(NestedProtectBegin)
    NetAliasCommonNetType: typing.ClassVar[DiagCode]  # value = DiagCode(NetAliasCommonNetType)
    NetAliasHierarchical: typing.ClassVar[DiagCode]  # value = DiagCode(NetAliasHierarchical)
    NetAliasNotANet: typing.ClassVar[DiagCode]  # value = DiagCode(NetAliasNotANet)
    NetAliasSelf: typing.ClassVar[DiagCode]  # value = DiagCode(NetAliasSelf)
    NetAliasWidthMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(NetAliasWidthMismatch)
    NetInconsistent: typing.ClassVar[DiagCode]  # value = DiagCode(NetInconsistent)
    NetRangeInconsistent: typing.ClassVar[DiagCode]  # value = DiagCode(NetRangeInconsistent)
    NewArrayTarget: typing.ClassVar[DiagCode]  # value = DiagCode(NewArrayTarget)
    NewClassTarget: typing.ClassVar[DiagCode]  # value = DiagCode(NewClassTarget)
    NewInterfaceClass: typing.ClassVar[DiagCode]  # value = DiagCode(NewInterfaceClass)
    NewKeywordQualified: typing.ClassVar[DiagCode]  # value = DiagCode(NewKeywordQualified)
    NewVirtualClass: typing.ClassVar[DiagCode]  # value = DiagCode(NewVirtualClass)
    NoChangeEdgeRequired: typing.ClassVar[DiagCode]  # value = DiagCode(NoChangeEdgeRequired)
    NoCommaInList: typing.ClassVar[DiagCode]  # value = DiagCode(NoCommaInList)
    NoCommonComparisonType: typing.ClassVar[DiagCode]  # value = DiagCode(NoCommonComparisonType)
    NoConstraintBody: typing.ClassVar[DiagCode]  # value = DiagCode(NoConstraintBody)
    NoDeclInClass: typing.ClassVar[DiagCode]  # value = DiagCode(NoDeclInClass)
    NoDefaultClocking: typing.ClassVar[DiagCode]  # value = DiagCode(NoDefaultClocking)
    NoDefaultSpecialization: typing.ClassVar[DiagCode]  # value = DiagCode(NoDefaultSpecialization)
    NoGlobalClocking: typing.ClassVar[DiagCode]  # value = DiagCode(NoGlobalClocking)
    NoImplicitConversion: typing.ClassVar[DiagCode]  # value = DiagCode(NoImplicitConversion)
    NoLabelOnSemicolon: typing.ClassVar[DiagCode]  # value = DiagCode(NoLabelOnSemicolon)
    NoMemberImplFound: typing.ClassVar[DiagCode]  # value = DiagCode(NoMemberImplFound)
    NoTopModules: typing.ClassVar[DiagCode]  # value = DiagCode(NoTopModules)
    NonIntegralConstraintLiteral: typing.ClassVar[DiagCode]  # value = DiagCode(NonIntegralConstraintLiteral)
    NonPrintableChar: typing.ClassVar[DiagCode]  # value = DiagCode(NonPrintableChar)
    NonProceduralFuncArg: typing.ClassVar[DiagCode]  # value = DiagCode(NonProceduralFuncArg)
    NonStandardGenBlock: typing.ClassVar[DiagCode]  # value = DiagCode(NonStandardGenBlock)
    NonStaticClassMethod: typing.ClassVar[DiagCode]  # value = DiagCode(NonStaticClassMethod)
    NonStaticClassProperty: typing.ClassVar[DiagCode]  # value = DiagCode(NonStaticClassProperty)
    NonblockingAssignmentToAuto: typing.ClassVar[DiagCode]  # value = DiagCode(NonblockingAssignmentToAuto)
    NonblockingDynamicAssign: typing.ClassVar[DiagCode]  # value = DiagCode(NonblockingDynamicAssign)
    NonblockingInFinal: typing.ClassVar[DiagCode]  # value = DiagCode(NonblockingInFinal)
    NonstandardDist: typing.ClassVar[DiagCode]  # value = DiagCode(NonstandardDist)
    NonstandardEscapeCode: typing.ClassVar[DiagCode]  # value = DiagCode(NonstandardEscapeCode)
    NonstandardForeach: typing.ClassVar[DiagCode]  # value = DiagCode(NonstandardForeach)
    NonstandardSysFunc: typing.ClassVar[DiagCode]  # value = DiagCode(NonstandardSysFunc)
    NotAChecker: typing.ClassVar[DiagCode]  # value = DiagCode(NotAChecker)
    NotAClass: typing.ClassVar[DiagCode]  # value = DiagCode(NotAClass)
    NotAClockingBlock: typing.ClassVar[DiagCode]  # value = DiagCode(NotAClockingBlock)
    NotAGenericClass: typing.ClassVar[DiagCode]  # value = DiagCode(NotAGenericClass)
    NotAGenvar: typing.ClassVar[DiagCode]  # value = DiagCode(NotAGenvar)
    NotAHierarchicalScope: typing.ClassVar[DiagCode]  # value = DiagCode(NotAHierarchicalScope)
    NotAModport: typing.ClassVar[DiagCode]  # value = DiagCode(NotAModport)
    NotAProduction: typing.ClassVar[DiagCode]  # value = DiagCode(NotAProduction)
    NotASubroutine: typing.ClassVar[DiagCode]  # value = DiagCode(NotASubroutine)
    NotAType: typing.ClassVar[DiagCode]  # value = DiagCode(NotAType)
    NotAValue: typing.ClassVar[DiagCode]  # value = DiagCode(NotAValue)
    NotAllowedInAnonymousProgram: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInAnonymousProgram)
    NotAllowedInCU: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInCU)
    NotAllowedInChecker: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInChecker)
    NotAllowedInClass: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInClass)
    NotAllowedInClocking: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInClocking)
    NotAllowedInGenerate: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInGenerate)
    NotAllowedInIfaceClass: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInIfaceClass)
    NotAllowedInInterface: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInInterface)
    NotAllowedInModport: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInModport)
    NotAllowedInModule: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInModule)
    NotAllowedInPackage: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInPackage)
    NotAllowedInProgram: typing.ClassVar[DiagCode]  # value = DiagCode(NotAllowedInProgram)
    NotAnArray: typing.ClassVar[DiagCode]  # value = DiagCode(NotAnArray)
    NotAnEvent: typing.ClassVar[DiagCode]  # value = DiagCode(NotAnEvent)
    NotAnInterface: typing.ClassVar[DiagCode]  # value = DiagCode(NotAnInterface)
    NotAnInterfaceOrPort: typing.ClassVar[DiagCode]  # value = DiagCode(NotAnInterfaceOrPort)
    NotBooleanConvertible: typing.ClassVar[DiagCode]  # value = DiagCode(NotBooleanConvertible)
    NotEnoughMacroArgs: typing.ClassVar[DiagCode]  # value = DiagCode(NotEnoughMacroArgs)
    NoteAliasDeclaration: typing.ClassVar[DiagCode]  # value = DiagCode(NoteAliasDeclaration)
    NoteAliasedTo: typing.ClassVar[DiagCode]  # value = DiagCode(NoteAliasedTo)
    NoteAlwaysFalse: typing.ClassVar[DiagCode]  # value = DiagCode(NoteAlwaysFalse)
    NoteAssignedHere: typing.ClassVar[DiagCode]  # value = DiagCode(NoteAssignedHere)
    NoteCommonAncestor: typing.ClassVar[DiagCode]  # value = DiagCode(NoteCommonAncestor)
    NoteComparisonReduces: typing.ClassVar[DiagCode]  # value = DiagCode(NoteComparisonReduces)
    NoteConditionalPrecedenceFix: typing.ClassVar[DiagCode]  # value = DiagCode(NoteConditionalPrecedenceFix)
    NoteConfigRule: typing.ClassVar[DiagCode]  # value = DiagCode(NoteConfigRule)
    NoteDeclarationHere: typing.ClassVar[DiagCode]  # value = DiagCode(NoteDeclarationHere)
    NoteDirectiveHere: typing.ClassVar[DiagCode]  # value = DiagCode(NoteDirectiveHere)
    NoteDrivenHere: typing.ClassVar[DiagCode]  # value = DiagCode(NoteDrivenHere)
    NoteExpandedHere: typing.ClassVar[DiagCode]  # value = DiagCode(NoteExpandedHere)
    NoteFromHere2: typing.ClassVar[DiagCode]  # value = DiagCode(NoteFromHere2)
    NoteHierarchicalRef: typing.ClassVar[DiagCode]  # value = DiagCode(NoteHierarchicalRef)
    NoteImportedFrom: typing.ClassVar[DiagCode]  # value = DiagCode(NoteImportedFrom)
    NoteInCallTo: typing.ClassVar[DiagCode]  # value = DiagCode(NoteInCallTo)
    NoteLastBlockEnded: typing.ClassVar[DiagCode]  # value = DiagCode(NoteLastBlockEnded)
    NoteLastBlockStarted: typing.ClassVar[DiagCode]  # value = DiagCode(NoteLastBlockStarted)
    NoteLogicalNotFix: typing.ClassVar[DiagCode]  # value = DiagCode(NoteLogicalNotFix)
    NoteLogicalNotSilence: typing.ClassVar[DiagCode]  # value = DiagCode(NoteLogicalNotSilence)
    NoteOriginalAssign: typing.ClassVar[DiagCode]  # value = DiagCode(NoteOriginalAssign)
    NotePrecedenceBitwiseFirst: typing.ClassVar[DiagCode]  # value = DiagCode(NotePrecedenceBitwiseFirst)
    NotePrecedenceSilence: typing.ClassVar[DiagCode]  # value = DiagCode(NotePrecedenceSilence)
    NotePreviousDefinition: typing.ClassVar[DiagCode]  # value = DiagCode(NotePreviousDefinition)
    NotePreviousMatch: typing.ClassVar[DiagCode]  # value = DiagCode(NotePreviousMatch)
    NotePreviousUsage: typing.ClassVar[DiagCode]  # value = DiagCode(NotePreviousUsage)
    NoteReferencedHere: typing.ClassVar[DiagCode]  # value = DiagCode(NoteReferencedHere)
    NoteSkippingFrames: typing.ClassVar[DiagCode]  # value = DiagCode(NoteSkippingFrames)
    NoteToMatchThis: typing.ClassVar[DiagCode]  # value = DiagCode(NoteToMatchThis)
    NoteUdpCoverage: typing.ClassVar[DiagCode]  # value = DiagCode(NoteUdpCoverage)
    NoteWhileExpanding: typing.ClassVar[DiagCode]  # value = DiagCode(NoteWhileExpanding)
    NullPortExpression: typing.ClassVar[DiagCode]  # value = DiagCode(NullPortExpression)
    ObjectTooLarge: typing.ClassVar[DiagCode]  # value = DiagCode(ObjectTooLarge)
    OctalEscapeCodeTooBig: typing.ClassVar[DiagCode]  # value = DiagCode(OctalEscapeCodeTooBig)
    OutRefFuncConstraint: typing.ClassVar[DiagCode]  # value = DiagCode(OutRefFuncConstraint)
    OutputPortCoercion: typing.ClassVar[DiagCode]  # value = DiagCode(OutputPortCoercion)
    OverridingExtends: typing.ClassVar[DiagCode]  # value = DiagCode(OverridingExtends)
    OverridingFinal: typing.ClassVar[DiagCode]  # value = DiagCode(OverridingFinal)
    OverridingInitial: typing.ClassVar[DiagCode]  # value = DiagCode(OverridingInitial)
    PackageExportSelf: typing.ClassVar[DiagCode]  # value = DiagCode(PackageExportSelf)
    PackageImportSelf: typing.ClassVar[DiagCode]  # value = DiagCode(PackageImportSelf)
    PackageNetInit: typing.ClassVar[DiagCode]  # value = DiagCode(PackageNetInit)
    PackedArrayConv: typing.ClassVar[DiagCode]  # value = DiagCode(PackedArrayConv)
    PackedArrayNotIntegral: typing.ClassVar[DiagCode]  # value = DiagCode(PackedArrayNotIntegral)
    PackedDimsOnPredefinedType: typing.ClassVar[DiagCode]  # value = DiagCode(PackedDimsOnPredefinedType)
    PackedDimsOnUnpacked: typing.ClassVar[DiagCode]  # value = DiagCode(PackedDimsOnUnpacked)
    PackedDimsRequireFullRange: typing.ClassVar[DiagCode]  # value = DiagCode(PackedDimsRequireFullRange)
    PackedMemberHasInitializer: typing.ClassVar[DiagCode]  # value = DiagCode(PackedMemberHasInitializer)
    PackedMemberNotIntegral: typing.ClassVar[DiagCode]  # value = DiagCode(PackedMemberNotIntegral)
    PackedTypeTooLarge: typing.ClassVar[DiagCode]  # value = DiagCode(PackedTypeTooLarge)
    PackedUnionWidthMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(PackedUnionWidthMismatch)
    ParallelPathWidth: typing.ClassVar[DiagCode]  # value = DiagCode(ParallelPathWidth)
    ParamHasNoValue: typing.ClassVar[DiagCode]  # value = DiagCode(ParamHasNoValue)
    ParameterDoesNotExist: typing.ClassVar[DiagCode]  # value = DiagCode(ParameterDoesNotExist)
    ParseTreeTooDeep: typing.ClassVar[DiagCode]  # value = DiagCode(ParseTreeTooDeep)
    PastNumTicksInvalid: typing.ClassVar[DiagCode]  # value = DiagCode(PastNumTicksInvalid)
    PathPulseInExpr: typing.ClassVar[DiagCode]  # value = DiagCode(PathPulseInExpr)
    PathPulseInvalidPathName: typing.ClassVar[DiagCode]  # value = DiagCode(PathPulseInvalidPathName)
    PatternStructTooFew: typing.ClassVar[DiagCode]  # value = DiagCode(PatternStructTooFew)
    PatternStructTooMany: typing.ClassVar[DiagCode]  # value = DiagCode(PatternStructTooMany)
    PatternStructType: typing.ClassVar[DiagCode]  # value = DiagCode(PatternStructType)
    PatternTaggedType: typing.ClassVar[DiagCode]  # value = DiagCode(PatternTaggedType)
    PlaRangeInAscendingOrder: typing.ClassVar[DiagCode]  # value = DiagCode(PlaRangeInAscendingOrder)
    PointlessVoidCast: typing.ClassVar[DiagCode]  # value = DiagCode(PointlessVoidCast)
    PortConcatInOut: typing.ClassVar[DiagCode]  # value = DiagCode(PortConcatInOut)
    PortConcatRef: typing.ClassVar[DiagCode]  # value = DiagCode(PortConcatRef)
    PortConnArrayMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(PortConnArrayMismatch)
    PortConnDimensionsMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(PortConnDimensionsMismatch)
    PortDeclDimensionsMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(PortDeclDimensionsMismatch)
    PortDeclInANSIModule: typing.ClassVar[DiagCode]  # value = DiagCode(PortDeclInANSIModule)
    PortDoesNotExist: typing.ClassVar[DiagCode]  # value = DiagCode(PortDoesNotExist)
    PortTypeNotInterfaceOrData: typing.ClassVar[DiagCode]  # value = DiagCode(PortTypeNotInterfaceOrData)
    PortWidthExpand: typing.ClassVar[DiagCode]  # value = DiagCode(PortWidthExpand)
    PortWidthTruncate: typing.ClassVar[DiagCode]  # value = DiagCode(PortWidthTruncate)
    PrimitiveAnsiMix: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitiveAnsiMix)
    PrimitiveDupInitial: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitiveDupInitial)
    PrimitiveDupOutput: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitiveDupOutput)
    PrimitiveInitVal: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitiveInitVal)
    PrimitiveInitialInComb: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitiveInitialInComb)
    PrimitiveOutputFirst: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitiveOutputFirst)
    PrimitivePortCountWrong: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitivePortCountWrong)
    PrimitivePortDup: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitivePortDup)
    PrimitivePortMissing: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitivePortMissing)
    PrimitivePortUnknown: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitivePortUnknown)
    PrimitiveRegDup: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitiveRegDup)
    PrimitiveRegInput: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitiveRegInput)
    PrimitiveTwoPorts: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitiveTwoPorts)
    PrimitiveWrongInitial: typing.ClassVar[DiagCode]  # value = DiagCode(PrimitiveWrongInitial)
    PropAbortLocalVar: typing.ClassVar[DiagCode]  # value = DiagCode(PropAbortLocalVar)
    PropAbortMatched: typing.ClassVar[DiagCode]  # value = DiagCode(PropAbortMatched)
    PropExprInSequence: typing.ClassVar[DiagCode]  # value = DiagCode(PropExprInSequence)
    PropInstanceRepetition: typing.ClassVar[DiagCode]  # value = DiagCode(PropInstanceRepetition)
    PropertyLhsInvalid: typing.ClassVar[DiagCode]  # value = DiagCode(PropertyLhsInvalid)
    PropertyPortInLet: typing.ClassVar[DiagCode]  # value = DiagCode(PropertyPortInLet)
    PropertyPortInSeq: typing.ClassVar[DiagCode]  # value = DiagCode(PropertyPortInSeq)
    ProtectArgList: typing.ClassVar[DiagCode]  # value = DiagCode(ProtectArgList)
    ProtectEncodingBytes: typing.ClassVar[DiagCode]  # value = DiagCode(ProtectEncodingBytes)
    ProtectedEnvelope: typing.ClassVar[DiagCode]  # value = DiagCode(ProtectedEnvelope)
    ProtectedMemberAccess: typing.ClassVar[DiagCode]  # value = DiagCode(ProtectedMemberAccess)
    PullStrengthHighZ: typing.ClassVar[DiagCode]  # value = DiagCode(PullStrengthHighZ)
    PulseControlPATHPULSE: typing.ClassVar[DiagCode]  # value = DiagCode(PulseControlPATHPULSE)
    PulseControlSpecifyParent: typing.ClassVar[DiagCode]  # value = DiagCode(PulseControlSpecifyParent)
    PureConstraintInAbstract: typing.ClassVar[DiagCode]  # value = DiagCode(PureConstraintInAbstract)
    PureInAbstract: typing.ClassVar[DiagCode]  # value = DiagCode(PureInAbstract)
    PureRequiresVirtual: typing.ClassVar[DiagCode]  # value = DiagCode(PureRequiresVirtual)
    QualifierConflict: typing.ClassVar[DiagCode]  # value = DiagCode(QualifierConflict)
    QualifierNotFirst: typing.ClassVar[DiagCode]  # value = DiagCode(QualifierNotFirst)
    QualifiersOnOutOfBlock: typing.ClassVar[DiagCode]  # value = DiagCode(QualifiersOnOutOfBlock)
    QueryOnAssociativeNonIntegral: typing.ClassVar[DiagCode]  # value = DiagCode(QueryOnAssociativeNonIntegral)
    QueryOnAssociativeWildcard: typing.ClassVar[DiagCode]  # value = DiagCode(QueryOnAssociativeWildcard)
    QueryOnDynamicType: typing.ClassVar[DiagCode]  # value = DiagCode(QueryOnDynamicType)
    RandCInDist: typing.ClassVar[DiagCode]  # value = DiagCode(RandCInDist)
    RandCInSoft: typing.ClassVar[DiagCode]  # value = DiagCode(RandCInSoft)
    RandCInSolveBefore: typing.ClassVar[DiagCode]  # value = DiagCode(RandCInSolveBefore)
    RandCInUnique: typing.ClassVar[DiagCode]  # value = DiagCode(RandCInUnique)
    RandJoinNotEnough: typing.ClassVar[DiagCode]  # value = DiagCode(RandJoinNotEnough)
    RandJoinNotNumeric: typing.ClassVar[DiagCode]  # value = DiagCode(RandJoinNotNumeric)
    RandJoinProdItem: typing.ClassVar[DiagCode]  # value = DiagCode(RandJoinProdItem)
    RandNeededInDist: typing.ClassVar[DiagCode]  # value = DiagCode(RandNeededInDist)
    RandOnPackedMember: typing.ClassVar[DiagCode]  # value = DiagCode(RandOnPackedMember)
    RandOnUnionMember: typing.ClassVar[DiagCode]  # value = DiagCode(RandOnUnionMember)
    RangeOOB: typing.ClassVar[DiagCode]  # value = DiagCode(RangeOOB)
    RangeSelectAssociative: typing.ClassVar[DiagCode]  # value = DiagCode(RangeSelectAssociative)
    RangeWidthOOB: typing.ClassVar[DiagCode]  # value = DiagCode(RangeWidthOOB)
    RangeWidthOverflow: typing.ClassVar[DiagCode]  # value = DiagCode(RangeWidthOverflow)
    RawProtectEOF: typing.ClassVar[DiagCode]  # value = DiagCode(RawProtectEOF)
    RealCoverpointBins: typing.ClassVar[DiagCode]  # value = DiagCode(RealCoverpointBins)
    RealCoverpointDefaultArray: typing.ClassVar[DiagCode]  # value = DiagCode(RealCoverpointDefaultArray)
    RealCoverpointImplicit: typing.ClassVar[DiagCode]  # value = DiagCode(RealCoverpointImplicit)
    RealCoverpointTransBins: typing.ClassVar[DiagCode]  # value = DiagCode(RealCoverpointTransBins)
    RealCoverpointWildcardBins: typing.ClassVar[DiagCode]  # value = DiagCode(RealCoverpointWildcardBins)
    RealCoverpointWithExpr: typing.ClassVar[DiagCode]  # value = DiagCode(RealCoverpointWithExpr)
    RealLiteralOverflow: typing.ClassVar[DiagCode]  # value = DiagCode(RealLiteralOverflow)
    RealLiteralUnderflow: typing.ClassVar[DiagCode]  # value = DiagCode(RealLiteralUnderflow)
    RecursiveClassSpecialization: typing.ClassVar[DiagCode]  # value = DiagCode(RecursiveClassSpecialization)
    RecursiveDefinition: typing.ClassVar[DiagCode]  # value = DiagCode(RecursiveDefinition)
    RecursiveLet: typing.ClassVar[DiagCode]  # value = DiagCode(RecursiveLet)
    RecursiveMacro: typing.ClassVar[DiagCode]  # value = DiagCode(RecursiveMacro)
    RecursivePropArgExpr: typing.ClassVar[DiagCode]  # value = DiagCode(RecursivePropArgExpr)
    RecursivePropDisableIff: typing.ClassVar[DiagCode]  # value = DiagCode(RecursivePropDisableIff)
    RecursivePropNegation: typing.ClassVar[DiagCode]  # value = DiagCode(RecursivePropNegation)
    RecursivePropTimeAdvance: typing.ClassVar[DiagCode]  # value = DiagCode(RecursivePropTimeAdvance)
    RecursiveSequence: typing.ClassVar[DiagCode]  # value = DiagCode(RecursiveSequence)
    RedefiningMacro: typing.ClassVar[DiagCode]  # value = DiagCode(RedefiningMacro)
    Redefinition: typing.ClassVar[DiagCode]  # value = DiagCode(Redefinition)
    RedefinitionDifferentType: typing.ClassVar[DiagCode]  # value = DiagCode(RedefinitionDifferentType)
    RefArgAutomaticFunc: typing.ClassVar[DiagCode]  # value = DiagCode(RefArgAutomaticFunc)
    RefArgForkJoin: typing.ClassVar[DiagCode]  # value = DiagCode(RefArgForkJoin)
    RefPortMustBeVariable: typing.ClassVar[DiagCode]  # value = DiagCode(RefPortMustBeVariable)
    RefPortUnconnected: typing.ClassVar[DiagCode]  # value = DiagCode(RefPortUnconnected)
    RefPortUnnamedUnconnected: typing.ClassVar[DiagCode]  # value = DiagCode(RefPortUnnamedUnconnected)
    RefTypeMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(RefTypeMismatch)
    RegAfterNettype: typing.ClassVar[DiagCode]  # value = DiagCode(RegAfterNettype)
    RepeatControlNotEvent: typing.ClassVar[DiagCode]  # value = DiagCode(RepeatControlNotEvent)
    RepeatNotNumeric: typing.ClassVar[DiagCode]  # value = DiagCode(RepeatNotNumeric)
    ReplicationZeroOutsideConcat: typing.ClassVar[DiagCode]  # value = DiagCode(ReplicationZeroOutsideConcat)
    RestrictStmtNoFail: typing.ClassVar[DiagCode]  # value = DiagCode(RestrictStmtNoFail)
    ReturnInParallel: typing.ClassVar[DiagCode]  # value = DiagCode(ReturnInParallel)
    ReturnNotInSubroutine: typing.ClassVar[DiagCode]  # value = DiagCode(ReturnNotInSubroutine)
    ReversedValueRange: typing.ClassVar[DiagCode]  # value = DiagCode(ReversedValueRange)
    SampledValueLocalVar: typing.ClassVar[DiagCode]  # value = DiagCode(SampledValueLocalVar)
    SampledValueMatched: typing.ClassVar[DiagCode]  # value = DiagCode(SampledValueMatched)
    ScopeIncompleteTypedef: typing.ClassVar[DiagCode]  # value = DiagCode(ScopeIncompleteTypedef)
    ScopeIndexOutOfRange: typing.ClassVar[DiagCode]  # value = DiagCode(ScopeIndexOutOfRange)
    ScopeNotIndexable: typing.ClassVar[DiagCode]  # value = DiagCode(ScopeNotIndexable)
    ScopedClassCopy: typing.ClassVar[DiagCode]  # value = DiagCode(ScopedClassCopy)
    SelectAfterRangeSelect: typing.ClassVar[DiagCode]  # value = DiagCode(SelectAfterRangeSelect)
    SelectEndianDynamic: typing.ClassVar[DiagCode]  # value = DiagCode(SelectEndianDynamic)
    SelectEndianMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(SelectEndianMismatch)
    SelectOfVectoredNet: typing.ClassVar[DiagCode]  # value = DiagCode(SelectOfVectoredNet)
    SeqEmptyMatch: typing.ClassVar[DiagCode]  # value = DiagCode(SeqEmptyMatch)
    SeqInstanceRepetition: typing.ClassVar[DiagCode]  # value = DiagCode(SeqInstanceRepetition)
    SeqMethodInputLocalVar: typing.ClassVar[DiagCode]  # value = DiagCode(SeqMethodInputLocalVar)
    SeqNoMatch: typing.ClassVar[DiagCode]  # value = DiagCode(SeqNoMatch)
    SeqOnlyEmpty: typing.ClassVar[DiagCode]  # value = DiagCode(SeqOnlyEmpty)
    SeqRangeMinMax: typing.ClassVar[DiagCode]  # value = DiagCode(SeqRangeMinMax)
    SequenceMethodLocalVar: typing.ClassVar[DiagCode]  # value = DiagCode(SequenceMethodLocalVar)
    SignCompare: typing.ClassVar[DiagCode]  # value = DiagCode(SignCompare)
    SignConversion: typing.ClassVar[DiagCode]  # value = DiagCode(SignConversion)
    SignedIntegerOverflow: typing.ClassVar[DiagCode]  # value = DiagCode(SignedIntegerOverflow)
    SignednessNoEffect: typing.ClassVar[DiagCode]  # value = DiagCode(SignednessNoEffect)
    SingleBitVectored: typing.ClassVar[DiagCode]  # value = DiagCode(SingleBitVectored)
    SolveBeforeDisallowed: typing.ClassVar[DiagCode]  # value = DiagCode(SolveBeforeDisallowed)
    SpecifiersNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(SpecifiersNotAllowed)
    SpecifyBlockParam: typing.ClassVar[DiagCode]  # value = DiagCode(SpecifyBlockParam)
    SpecifyPathBadReference: typing.ClassVar[DiagCode]  # value = DiagCode(SpecifyPathBadReference)
    SpecifyPathConditionExpr: typing.ClassVar[DiagCode]  # value = DiagCode(SpecifyPathConditionExpr)
    SpecifyPathMultiDim: typing.ClassVar[DiagCode]  # value = DiagCode(SpecifyPathMultiDim)
    SpecparamInConstant: typing.ClassVar[DiagCode]  # value = DiagCode(SpecparamInConstant)
    SplitDistWeightOp: typing.ClassVar[DiagCode]  # value = DiagCode(SplitDistWeightOp)
    StatementNotInLoop: typing.ClassVar[DiagCode]  # value = DiagCode(StatementNotInLoop)
    StaticAssert: typing.ClassVar[DiagCode]  # value = DiagCode(StaticAssert)
    StaticConstNoInitializer: typing.ClassVar[DiagCode]  # value = DiagCode(StaticConstNoInitializer)
    StaticFuncSpecifier: typing.ClassVar[DiagCode]  # value = DiagCode(StaticFuncSpecifier)
    StaticInitOrder: typing.ClassVar[DiagCode]  # value = DiagCode(StaticInitOrder)
    StaticInitValue: typing.ClassVar[DiagCode]  # value = DiagCode(StaticInitValue)
    StaticInitializerMustBeExplicit: typing.ClassVar[DiagCode]  # value = DiagCode(StaticInitializerMustBeExplicit)
    SubroutineMatchAutoRefArg: typing.ClassVar[DiagCode]  # value = DiagCode(SubroutineMatchAutoRefArg)
    SubroutineMatchNonVoid: typing.ClassVar[DiagCode]  # value = DiagCode(SubroutineMatchNonVoid)
    SubroutineMatchOutArg: typing.ClassVar[DiagCode]  # value = DiagCode(SubroutineMatchOutArg)
    SubroutinePortInitializer: typing.ClassVar[DiagCode]  # value = DiagCode(SubroutinePortInitializer)
    SubroutinePrototypeScoped: typing.ClassVar[DiagCode]  # value = DiagCode(SubroutinePrototypeScoped)
    SuperNoBase: typing.ClassVar[DiagCode]  # value = DiagCode(SuperNoBase)
    SuperOutsideClass: typing.ClassVar[DiagCode]  # value = DiagCode(SuperOutsideClass)
    SysFuncHierarchicalNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(SysFuncHierarchicalNotAllowed)
    SysFuncNotConst: typing.ClassVar[DiagCode]  # value = DiagCode(SysFuncNotConst)
    TaggedStruct: typing.ClassVar[DiagCode]  # value = DiagCode(TaggedStruct)
    TaggedUnionMissingInit: typing.ClassVar[DiagCode]  # value = DiagCode(TaggedUnionMissingInit)
    TaggedUnionTarget: typing.ClassVar[DiagCode]  # value = DiagCode(TaggedUnionTarget)
    TaskConstructor: typing.ClassVar[DiagCode]  # value = DiagCode(TaskConstructor)
    TaskFromFinal: typing.ClassVar[DiagCode]  # value = DiagCode(TaskFromFinal)
    TaskFromFunction: typing.ClassVar[DiagCode]  # value = DiagCode(TaskFromFunction)
    TaskInConstraint: typing.ClassVar[DiagCode]  # value = DiagCode(TaskInConstraint)
    TaskReturnType: typing.ClassVar[DiagCode]  # value = DiagCode(TaskReturnType)
    ThroughoutLhsInvalid: typing.ClassVar[DiagCode]  # value = DiagCode(ThroughoutLhsInvalid)
    TimeScaleFirstInScope: typing.ClassVar[DiagCode]  # value = DiagCode(TimeScaleFirstInScope)
    TimingCheckEventEdgeRequired: typing.ClassVar[DiagCode]  # value = DiagCode(TimingCheckEventEdgeRequired)
    TimingCheckEventNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(TimingCheckEventNotAllowed)
    TimingControlNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(TimingControlNotAllowed)
    TimingInFuncNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(TimingInFuncNotAllowed)
    TooFewArguments: typing.ClassVar[DiagCode]  # value = DiagCode(TooFewArguments)
    TooManyActualMacroArgs: typing.ClassVar[DiagCode]  # value = DiagCode(TooManyActualMacroArgs)
    TooManyArguments: typing.ClassVar[DiagCode]  # value = DiagCode(TooManyArguments)
    TooManyEdgeDescriptors: typing.ClassVar[DiagCode]  # value = DiagCode(TooManyEdgeDescriptors)
    TooManyErrors: typing.ClassVar[DiagCode]  # value = DiagCode(TooManyErrors)
    TooManyForeachVars: typing.ClassVar[DiagCode]  # value = DiagCode(TooManyForeachVars)
    TooManyLexerErrors: typing.ClassVar[DiagCode]  # value = DiagCode(TooManyLexerErrors)
    TooManyParamAssignments: typing.ClassVar[DiagCode]  # value = DiagCode(TooManyParamAssignments)
    TooManyPortConnections: typing.ClassVar[DiagCode]  # value = DiagCode(TooManyPortConnections)
    TopModuleIfacePort: typing.ClassVar[DiagCode]  # value = DiagCode(TopModuleIfacePort)
    TopModuleRefPort: typing.ClassVar[DiagCode]  # value = DiagCode(TopModuleRefPort)
    TopModuleUnnamedRefPort: typing.ClassVar[DiagCode]  # value = DiagCode(TopModuleUnnamedRefPort)
    TypeHierarchical: typing.ClassVar[DiagCode]  # value = DiagCode(TypeHierarchical)
    TypeIsNotAClass: typing.ClassVar[DiagCode]  # value = DiagCode(TypeIsNotAClass)
    TypeRefDeclVar: typing.ClassVar[DiagCode]  # value = DiagCode(TypeRefDeclVar)
    TypeRefHierarchical: typing.ClassVar[DiagCode]  # value = DiagCode(TypeRefHierarchical)
    TypeRefVoid: typing.ClassVar[DiagCode]  # value = DiagCode(TypeRefVoid)
    TypeRestrictionMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(TypeRestrictionMismatch)
    TypoIdentifier: typing.ClassVar[DiagCode]  # value = DiagCode(TypoIdentifier)
    UTF8Char: typing.ClassVar[DiagCode]  # value = DiagCode(UTF8Char)
    UdpAllX: typing.ClassVar[DiagCode]  # value = DiagCode(UdpAllX)
    UdpCombState: typing.ClassVar[DiagCode]  # value = DiagCode(UdpCombState)
    UdpCoverage: typing.ClassVar[DiagCode]  # value = DiagCode(UdpCoverage)
    UdpDupDiffOutput: typing.ClassVar[DiagCode]  # value = DiagCode(UdpDupDiffOutput)
    UdpDupTransition: typing.ClassVar[DiagCode]  # value = DiagCode(UdpDupTransition)
    UdpEdgeInComb: typing.ClassVar[DiagCode]  # value = DiagCode(UdpEdgeInComb)
    UdpInvalidEdgeSymbol: typing.ClassVar[DiagCode]  # value = DiagCode(UdpInvalidEdgeSymbol)
    UdpInvalidInputOnly: typing.ClassVar[DiagCode]  # value = DiagCode(UdpInvalidInputOnly)
    UdpInvalidMinus: typing.ClassVar[DiagCode]  # value = DiagCode(UdpInvalidMinus)
    UdpInvalidOutput: typing.ClassVar[DiagCode]  # value = DiagCode(UdpInvalidOutput)
    UdpInvalidSymbol: typing.ClassVar[DiagCode]  # value = DiagCode(UdpInvalidSymbol)
    UdpInvalidTransition: typing.ClassVar[DiagCode]  # value = DiagCode(UdpInvalidTransition)
    UdpSequentialState: typing.ClassVar[DiagCode]  # value = DiagCode(UdpSequentialState)
    UdpSingleChar: typing.ClassVar[DiagCode]  # value = DiagCode(UdpSingleChar)
    UdpTransSameChar: typing.ClassVar[DiagCode]  # value = DiagCode(UdpTransSameChar)
    UdpTransitionLength: typing.ClassVar[DiagCode]  # value = DiagCode(UdpTransitionLength)
    UdpWrongInputCount: typing.ClassVar[DiagCode]  # value = DiagCode(UdpWrongInputCount)
    UnassignedVariable: typing.ClassVar[DiagCode]  # value = DiagCode(UnassignedVariable)
    UnbalancedMacroArgDims: typing.ClassVar[DiagCode]  # value = DiagCode(UnbalancedMacroArgDims)
    UnboundedNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(UnboundedNotAllowed)
    UnclosedTranslateOff: typing.ClassVar[DiagCode]  # value = DiagCode(UnclosedTranslateOff)
    UnconnectedArg: typing.ClassVar[DiagCode]  # value = DiagCode(UnconnectedArg)
    UnconnectedNamedPort: typing.ClassVar[DiagCode]  # value = DiagCode(UnconnectedNamedPort)
    UnconnectedUnnamedPort: typing.ClassVar[DiagCode]  # value = DiagCode(UnconnectedUnnamedPort)
    UndeclaredButFoundPackage: typing.ClassVar[DiagCode]  # value = DiagCode(UndeclaredButFoundPackage)
    UndeclaredIdentifier: typing.ClassVar[DiagCode]  # value = DiagCode(UndeclaredIdentifier)
    UndefineBuiltinDirective: typing.ClassVar[DiagCode]  # value = DiagCode(UndefineBuiltinDirective)
    UndrivenNet: typing.ClassVar[DiagCode]  # value = DiagCode(UndrivenNet)
    UndrivenPort: typing.ClassVar[DiagCode]  # value = DiagCode(UndrivenPort)
    UnexpectedClockingExpr: typing.ClassVar[DiagCode]  # value = DiagCode(UnexpectedClockingExpr)
    UnexpectedConditionalDirective: typing.ClassVar[DiagCode]  # value = DiagCode(UnexpectedConditionalDirective)
    UnexpectedConstraintBlock: typing.ClassVar[DiagCode]  # value = DiagCode(UnexpectedConstraintBlock)
    UnexpectedEndDelim: typing.ClassVar[DiagCode]  # value = DiagCode(UnexpectedEndDelim)
    UnexpectedLetPortKeyword: typing.ClassVar[DiagCode]  # value = DiagCode(UnexpectedLetPortKeyword)
    UnexpectedNameToken: typing.ClassVar[DiagCode]  # value = DiagCode(UnexpectedNameToken)
    UnexpectedPortDecl: typing.ClassVar[DiagCode]  # value = DiagCode(UnexpectedPortDecl)
    UnexpectedQualifiers: typing.ClassVar[DiagCode]  # value = DiagCode(UnexpectedQualifiers)
    UnexpectedSelection: typing.ClassVar[DiagCode]  # value = DiagCode(UnexpectedSelection)
    UnexpectedWithClause: typing.ClassVar[DiagCode]  # value = DiagCode(UnexpectedWithClause)
    UnicodeBOM: typing.ClassVar[DiagCode]  # value = DiagCode(UnicodeBOM)
    UniquePriorityAfterElse: typing.ClassVar[DiagCode]  # value = DiagCode(UniquePriorityAfterElse)
    UnknownClassMember: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownClassMember)
    UnknownClassOrPackage: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownClassOrPackage)
    UnknownConstraintLiteral: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownConstraintLiteral)
    UnknownCovergroupBase: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownCovergroupBase)
    UnknownCovergroupMember: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownCovergroupMember)
    UnknownDiagPragmaArg: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownDiagPragmaArg)
    UnknownDirective: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownDirective)
    UnknownEscapeCode: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownEscapeCode)
    UnknownFormatSpecifier: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownFormatSpecifier)
    UnknownInterface: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownInterface)
    UnknownLibrary: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownLibrary)
    UnknownMember: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownMember)
    UnknownModule: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownModule)
    UnknownPackage: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownPackage)
    UnknownPackageMember: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownPackageMember)
    UnknownPragma: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownPragma)
    UnknownPrimitive: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownPrimitive)
    UnknownProtectEncoding: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownProtectEncoding)
    UnknownProtectKeyword: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownProtectKeyword)
    UnknownProtectOption: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownProtectOption)
    UnknownSystemMethod: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownSystemMethod)
    UnknownSystemName: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownSystemName)
    UnknownSystemTimingCheck: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownSystemTimingCheck)
    UnknownWarningOption: typing.ClassVar[DiagCode]  # value = DiagCode(UnknownWarningOption)
    UnpackedArrayParamType: typing.ClassVar[DiagCode]  # value = DiagCode(UnpackedArrayParamType)
    UnpackedConcatAssociative: typing.ClassVar[DiagCode]  # value = DiagCode(UnpackedConcatAssociative)
    UnpackedConcatSize: typing.ClassVar[DiagCode]  # value = DiagCode(UnpackedConcatSize)
    UnpackedSigned: typing.ClassVar[DiagCode]  # value = DiagCode(UnpackedSigned)
    UnrecognizedKeywordVersion: typing.ClassVar[DiagCode]  # value = DiagCode(UnrecognizedKeywordVersion)
    UnresolvedForwardTypedef: typing.ClassVar[DiagCode]  # value = DiagCode(UnresolvedForwardTypedef)
    UnsignedArithShift: typing.ClassVar[DiagCode]  # value = DiagCode(UnsignedArithShift)
    UnsizedInConcat: typing.ClassVar[DiagCode]  # value = DiagCode(UnsizedInConcat)
    UnterminatedBlockComment: typing.ClassVar[DiagCode]  # value = DiagCode(UnterminatedBlockComment)
    UnusedArgument: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedArgument)
    UnusedAssertionDecl: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedAssertionDecl)
    UnusedButSetNet: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedButSetNet)
    UnusedButSetPort: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedButSetPort)
    UnusedButSetVariable: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedButSetVariable)
    UnusedConfigCell: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedConfigCell)
    UnusedConfigInstance: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedConfigInstance)
    UnusedDefinition: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedDefinition)
    UnusedGenvar: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedGenvar)
    UnusedImplicitNet: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedImplicitNet)
    UnusedImport: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedImport)
    UnusedNet: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedNet)
    UnusedParameter: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedParameter)
    UnusedPort: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedPort)
    UnusedPortDecl: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedPortDecl)
    UnusedResult: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedResult)
    UnusedTypeParameter: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedTypeParameter)
    UnusedTypedef: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedTypedef)
    UnusedVariable: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedVariable)
    UnusedWildcardImport: typing.ClassVar[DiagCode]  # value = DiagCode(UnusedWildcardImport)
    UsedBeforeDeclared: typing.ClassVar[DiagCode]  # value = DiagCode(UsedBeforeDeclared)
    UselessCast: typing.ClassVar[DiagCode]  # value = DiagCode(UselessCast)
    UserDefPartialDriver: typing.ClassVar[DiagCode]  # value = DiagCode(UserDefPartialDriver)
    UserDefPortMixedConcat: typing.ClassVar[DiagCode]  # value = DiagCode(UserDefPortMixedConcat)
    UserDefPortTwoSided: typing.ClassVar[DiagCode]  # value = DiagCode(UserDefPortTwoSided)
    ValueExceedsMaxBitWidth: typing.ClassVar[DiagCode]  # value = DiagCode(ValueExceedsMaxBitWidth)
    ValueMustBeIntegral: typing.ClassVar[DiagCode]  # value = DiagCode(ValueMustBeIntegral)
    ValueMustBePositive: typing.ClassVar[DiagCode]  # value = DiagCode(ValueMustBePositive)
    ValueMustNotBeUnknown: typing.ClassVar[DiagCode]  # value = DiagCode(ValueMustNotBeUnknown)
    ValueOutOfRange: typing.ClassVar[DiagCode]  # value = DiagCode(ValueOutOfRange)
    ValueRangeUnbounded: typing.ClassVar[DiagCode]  # value = DiagCode(ValueRangeUnbounded)
    VarDeclWithDelay: typing.ClassVar[DiagCode]  # value = DiagCode(VarDeclWithDelay)
    VarWithInterfacePort: typing.ClassVar[DiagCode]  # value = DiagCode(VarWithInterfacePort)
    VectorLiteralOverflow: typing.ClassVar[DiagCode]  # value = DiagCode(VectorLiteralOverflow)
    VirtualArgCountMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualArgCountMismatch)
    VirtualArgDirectionMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualArgDirectionMismatch)
    VirtualArgNameMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualArgNameMismatch)
    VirtualArgNoDerivedDefault: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualArgNoDerivedDefault)
    VirtualArgNoParentDefault: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualArgNoParentDefault)
    VirtualArgTypeMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualArgTypeMismatch)
    VirtualIfaceConfigRule: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualIfaceConfigRule)
    VirtualIfaceDefparam: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualIfaceDefparam)
    VirtualIfaceHierRef: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualIfaceHierRef)
    VirtualIfaceIfacePort: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualIfaceIfacePort)
    VirtualInterfaceIfaceMember: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualInterfaceIfaceMember)
    VirtualInterfaceUnionMember: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualInterfaceUnionMember)
    VirtualKindMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualKindMismatch)
    VirtualReturnMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualReturnMismatch)
    VirtualVisibilityMismatch: typing.ClassVar[DiagCode]  # value = DiagCode(VirtualVisibilityMismatch)
    VoidAssignment: typing.ClassVar[DiagCode]  # value = DiagCode(VoidAssignment)
    VoidCastFuncCall: typing.ClassVar[DiagCode]  # value = DiagCode(VoidCastFuncCall)
    VoidNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(VoidNotAllowed)
    WarnUnknownLibrary: typing.ClassVar[DiagCode]  # value = DiagCode(WarnUnknownLibrary)
    WarningTask: typing.ClassVar[DiagCode]  # value = DiagCode(WarningTask)
    WidthExpand: typing.ClassVar[DiagCode]  # value = DiagCode(WidthExpand)
    WidthTruncate: typing.ClassVar[DiagCode]  # value = DiagCode(WidthTruncate)
    WildcardPortGenericIface: typing.ClassVar[DiagCode]  # value = DiagCode(WildcardPortGenericIface)
    WireDataType: typing.ClassVar[DiagCode]  # value = DiagCode(WireDataType)
    WithClauseNotAllowed: typing.ClassVar[DiagCode]  # value = DiagCode(WithClauseNotAllowed)
    WriteToInputClockVar: typing.ClassVar[DiagCode]  # value = DiagCode(WriteToInputClockVar)
    WrongBindTargetDef: typing.ClassVar[DiagCode]  # value = DiagCode(WrongBindTargetDef)
    WrongLanguageVersion: typing.ClassVar[DiagCode]  # value = DiagCode(WrongLanguageVersion)
    WrongNumberAssignmentPatterns: typing.ClassVar[DiagCode]  # value = DiagCode(WrongNumberAssignmentPatterns)
    WrongSpecifyDelayCount: typing.ClassVar[DiagCode]  # value = DiagCode(WrongSpecifyDelayCount)
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DimensionKind:
    """
    Members:

      Unknown

      Range

      AbbreviatedRange

      Dynamic

      Associative

      Queue

      DPIOpenArray
    """
    AbbreviatedRange: typing.ClassVar[DimensionKind]  # value = <DimensionKind.AbbreviatedRange: 2>
    Associative: typing.ClassVar[DimensionKind]  # value = <DimensionKind.Associative: 4>
    DPIOpenArray: typing.ClassVar[DimensionKind]  # value = <DimensionKind.DPIOpenArray: 6>
    Dynamic: typing.ClassVar[DimensionKind]  # value = <DimensionKind.Dynamic: 3>
    Queue: typing.ClassVar[DimensionKind]  # value = <DimensionKind.Queue: 5>
    Range: typing.ClassVar[DimensionKind]  # value = <DimensionKind.Range: 1>
    Unknown: typing.ClassVar[DimensionKind]  # value = <DimensionKind.Unknown: 0>
    __members__: typing.ClassVar[dict[str, DimensionKind]]  # value = {'Unknown': <DimensionKind.Unknown: 0>, 'Range': <DimensionKind.Range: 1>, 'AbbreviatedRange': <DimensionKind.AbbreviatedRange: 2>, 'Dynamic': <DimensionKind.Dynamic: 3>, 'Associative': <DimensionKind.Associative: 4>, 'Queue': <DimensionKind.Queue: 5>, 'DPIOpenArray': <DimensionKind.DPIOpenArray: 6>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DimensionSpecifierSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DirectiveSyntax(SyntaxNode):
    directive: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DisableConstraintSyntax(ConstraintItemSyntax):
    disable: Token
    name: ExpressionSyntax
    semi: Token
    soft: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DisableForkStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DisableForkStatementSyntax(StatementSyntax):
    disable: Token
    fork: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DisableIffAssertionExpr(AssertionExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def condition(self) -> ...:
        ...
    @property
    def expr(self) -> AssertionExpr:
        ...
class DisableIffSyntax(SyntaxNode):
    closeParen: Token
    disable: Token
    expr: ExpressionSyntax
    iff: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DisableSoftConstraint(Constraint):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def target(self) -> ...:
        ...
class DisableStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def target(self) -> Expression:
        ...
class DisableStatementSyntax(StatementSyntax):
    disable: Token
    name: NameSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DistConstraintListSyntax(SyntaxNode):
    closeBrace: Token
    dist: Token
    items: ...
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DistExpression(Expression):
    class DistItem:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def value(self) -> Expression:
            ...
        @property
        def weight(self) -> DistExpression.DistWeight | None:
            ...
    class DistWeight:
        class Kind:
            """
            Members:

              PerValue

              PerRange
            """
            PerRange: typing.ClassVar[DistExpression.DistWeight.Kind]  # value = <Kind.PerRange: 1>
            PerValue: typing.ClassVar[DistExpression.DistWeight.Kind]  # value = <Kind.PerValue: 0>
            __members__: typing.ClassVar[dict[str, DistExpression.DistWeight.Kind]]  # value = {'PerValue': <Kind.PerValue: 0>, 'PerRange': <Kind.PerRange: 1>}
            @staticmethod
            def _pybind11_conduit_v1_(*args, **kwargs):
                ...
            def __eq__(self, other: typing.Any) -> bool:
                ...
            def __getstate__(self) -> int:
                ...
            def __hash__(self) -> int:
                ...
            def __index__(self) -> int:
                ...
            def __init__(self, value: int) -> None:
                ...
            def __int__(self) -> int:
                ...
            def __ne__(self, other: typing.Any) -> bool:
                ...
            def __repr__(self) -> str:
                ...
            def __setstate__(self, state: int) -> None:
                ...
            def __str__(self) -> str:
                ...
            @property
            def name(self) -> str:
                ...
            @property
            def value(self) -> int:
                ...
        PerRange: typing.ClassVar[DistExpression.DistWeight.Kind]  # value = <Kind.PerRange: 1>
        PerValue: typing.ClassVar[DistExpression.DistWeight.Kind]  # value = <Kind.PerValue: 0>
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def kind(self) -> ...:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def defaultWeight(self) -> ...:
        ...
    @property
    def items(self) -> span[...]:
        ...
    @property
    def left(self) -> Expression:
        ...
class DistItemBaseSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DistItemSyntax(DistItemBaseSyntax):
    range: ExpressionSyntax
    weight: DistWeightSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DistWeightSyntax(SyntaxNode):
    expr: ExpressionSyntax
    extraOp: Token
    op: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DividerClauseSyntax(SyntaxNode):
    divide: Token
    value: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DoWhileLoopStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def body(self) -> Statement:
        ...
    @property
    def cond(self) -> Expression:
        ...
class DoWhileStatementSyntax(StatementSyntax):
    closeParen: Token
    doKeyword: Token
    expr: ExpressionSyntax
    openParen: Token
    semi: Token
    statement: StatementSyntax
    whileKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DotMemberClauseSyntax(SyntaxNode):
    dot: Token
    member: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class DriveStrengthSyntax(NetStrengthSyntax):
    closeParen: Token
    comma: Token
    openParen: Token
    strength0: Token
    strength1: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class Driver:
    languageVersion: LanguageVersion
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def addStandardArgs(self) -> None:
        ...
    def createCompilation(self) -> Compilation:
        ...
    def createOptionBag(self) -> ...:
        ...
    def parseAllSources(self) -> bool:
        ...
    def parseCommandLine(self, arg: str, parseOptions: CommandLineOptions = ...) -> bool:
        ...
    def processCommandFiles(self, fileName: str, makeRelative: bool, separateUnit: bool) -> bool:
        ...
    def processOptions(self) -> bool:
        ...
    def reportCompilation(self, compilation: Compilation, quiet: bool) -> bool:
        ...
    def reportMacros(self) -> None:
        ...
    def reportParseDiags(self) -> bool:
        ...
    def runPreprocessor(self, includeComments: bool, includeDirectives: bool, obfuscateIds: bool, useFixedObfuscationSeed: bool = False) -> bool:
        ...
    @property
    def diagEngine(self) -> ...:
        ...
    @property
    def sourceLoader(self) -> ...:
        ...
    @property
    def sourceManager(self) -> ...:
        ...
    @property
    def syntaxTrees(self) -> list[...]:
        ...
    @property
    def textDiagClient(self) -> ...:
        ...
class DriverKind:
    """
    Members:

      Procedural

      Continuous

      Other
    """
    Continuous: typing.ClassVar[DriverKind]  # value = <DriverKind.Continuous: 1>
    Other: typing.ClassVar[DriverKind]  # value = <DriverKind.Other: 2>
    Procedural: typing.ClassVar[DriverKind]  # value = <DriverKind.Procedural: 0>
    __members__: typing.ClassVar[dict[str, DriverKind]]  # value = {'Procedural': <DriverKind.Procedural: 0>, 'Continuous': <DriverKind.Continuous: 1>, 'Other': <DriverKind.Other: 2>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DynamicArrayType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def elementType(self) -> Type:
        ...
class EdgeControlSpecifierSyntax(SyntaxNode):
    closeBracket: Token
    descriptors: ...
    openBracket: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EdgeDescriptorSyntax(SyntaxNode):
    t1: Token
    t2: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EdgeKind:
    """
    Members:

      None

      PosEdge

      NegEdge

      BothEdges
    """
    BothEdges: typing.ClassVar[EdgeKind]  # value = <EdgeKind.BothEdges: 3>
    NegEdge: typing.ClassVar[EdgeKind]  # value = <EdgeKind.NegEdge: 2>
    None: typing.ClassVar[EdgeKind]  # value = <EdgeKind.None: 0>
    PosEdge: typing.ClassVar[EdgeKind]  # value = <EdgeKind.PosEdge: 1>
    __members__: typing.ClassVar[dict[str, EdgeKind]]  # value = {'None': <EdgeKind.None: 0>, 'PosEdge': <EdgeKind.PosEdge: 1>, 'NegEdge': <EdgeKind.NegEdge: 2>, 'BothEdges': <EdgeKind.BothEdges: 3>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EdgeSensitivePathSuffixSyntax(PathSuffixSyntax):
    closeParen: Token
    colon: Token
    expr: ExpressionSyntax
    openParen: Token
    outputs: ...
    polarityOperator: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ElabSystemTaskKind:
    """
    Members:

      Fatal

      Error

      Warning

      Info

      StaticAssert
    """
    Error: typing.ClassVar[ElabSystemTaskKind]  # value = <ElabSystemTaskKind.Error: 1>
    Fatal: typing.ClassVar[ElabSystemTaskKind]  # value = <ElabSystemTaskKind.Fatal: 0>
    Info: typing.ClassVar[ElabSystemTaskKind]  # value = <ElabSystemTaskKind.Info: 3>
    StaticAssert: typing.ClassVar[ElabSystemTaskKind]  # value = <ElabSystemTaskKind.StaticAssert: 4>
    Warning: typing.ClassVar[ElabSystemTaskKind]  # value = <ElabSystemTaskKind.Warning: 2>
    __members__: typing.ClassVar[dict[str, ElabSystemTaskKind]]  # value = {'Fatal': <ElabSystemTaskKind.Fatal: 0>, 'Error': <ElabSystemTaskKind.Error: 1>, 'Warning': <ElabSystemTaskKind.Warning: 2>, 'Info': <ElabSystemTaskKind.Info: 3>, 'StaticAssert': <ElabSystemTaskKind.StaticAssert: 4>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ElabSystemTaskSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def assertCondition(self) -> Expression:
        ...
    @property
    def message(self) -> str | None:
        ...
    @property
    def taskKind(self) -> ElabSystemTaskKind:
        ...
class ElabSystemTaskSyntax(MemberSyntax):
    arguments: ArgumentListSyntax
    name: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ElementSelectExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def selector(self) -> Expression:
        ...
    @property
    def value(self) -> Expression:
        ...
class ElementSelectExpressionSyntax(ExpressionSyntax):
    left: ExpressionSyntax
    select: ElementSelectSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ElementSelectSyntax(SyntaxNode):
    closeBracket: Token
    openBracket: Token
    selector: SelectorSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ElseClauseSyntax(SyntaxNode):
    clause: SyntaxNode
    elseKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ElseConstraintClauseSyntax(SyntaxNode):
    constraints: ConstraintItemSyntax
    elseKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ElsePropertyClauseSyntax(SyntaxNode):
    elseKeyword: Token
    expr: PropertyExprSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EmptyArgumentExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EmptyArgumentSyntax(ArgumentSyntax):
    placeholder: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EmptyIdentifierNameSyntax(NameSyntax):
    placeholder: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EmptyMemberSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EmptyMemberSyntax(MemberSyntax):
    qualifiers: ...
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EmptyNonAnsiPortSyntax(NonAnsiPortSyntax):
    placeholder: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EmptyPortConnectionSyntax(PortConnectionSyntax):
    placeholder: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EmptyQueueExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EmptyStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EmptyStatementSyntax(StatementSyntax):
    semicolon: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EmptyTimingCheckArgSyntax(TimingCheckArgSyntax):
    placeholder: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EnumType(IntegralType, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def baseType(self) -> Type:
        ...
    @property
    def systemId(self) -> int:
        ...
class EnumTypeSyntax(DataTypeSyntax):
    baseType: DataTypeSyntax
    closeBrace: Token
    dimensions: ...
    keyword: Token
    members: ...
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EnumValueSymbol(ValueSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def value(self) -> ConstantValue:
        ...
class EqualsAssertionArgClauseSyntax(SyntaxNode):
    equals: Token
    expr: PropertyExprSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EqualsTypeClauseSyntax(SyntaxNode):
    equals: Token
    type: DataTypeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EqualsValueClauseSyntax(SyntaxNode):
    equals: Token
    expr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ErrorType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EvalContext:
    class Frame:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def callLocation(self) -> ...:
            ...
        @property
        def lookupLocation(self) -> ...:
            ...
        @property
        def subroutine(self) -> ...:
            ...
        @property
        def temporaries(self) -> dict[..., ...]:
            ...
    queueTarget: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, astCtx: ..., flags: EvalFlags = ...) -> None:
        ...
    def createLocal(self, symbol: ..., value: ... = None) -> ...:
        ...
    def deleteLocal(self, symbol: ...) -> None:
        ...
    def dumpStack(self) -> str:
        ...
    def findLocal(self, symbol: ...) -> ...:
        ...
    def popFrame(self) -> None:
        ...
    def popLValue(self) -> None:
        ...
    def pushEmptyFrame(self) -> None:
        ...
    def pushFrame(self, subroutine: ..., callLocation: ..., lookupLocation: ...) -> bool:
        ...
    def pushLValue(self, lval: ...) -> None:
        ...
    def setDisableTarget(self, arg0: ..., arg1: ...) -> None:
        ...
    def step(self, loc: ...) -> bool:
        ...
    @property
    def cacheResults(self) -> bool:
        ...
    @property
    def diagnostics(self) -> ...:
        ...
    @property
    def disableRange(self) -> ...:
        ...
    @property
    def disableTarget(self) -> ...:
        ...
    @property
    def flags(self) -> EvalFlags:
        ...
    @property
    def inFunction(self) -> bool:
        ...
    @property
    def topFrame(self) -> ...:
        ...
    @property
    def topLValue(self) -> ...:
        ...
class EvalFlags:
    """
    Members:

      None_

      IsScript

      CacheResults

      SpecparamsAllowed

      CovergroupExpr

      AllowUnboundedPlaceholder
    """
    AllowUnboundedPlaceholder: typing.ClassVar[EvalFlags]  # value = <EvalFlags.AllowUnboundedPlaceholder: 16>
    CacheResults: typing.ClassVar[EvalFlags]  # value = <EvalFlags.CacheResults: 2>
    CovergroupExpr: typing.ClassVar[EvalFlags]  # value = <EvalFlags.CovergroupExpr: 8>
    IsScript: typing.ClassVar[EvalFlags]  # value = <EvalFlags.IsScript: 1>
    None_: typing.ClassVar[EvalFlags]  # value = <EvalFlags.None_: 0>
    SpecparamsAllowed: typing.ClassVar[EvalFlags]  # value = <EvalFlags.SpecparamsAllowed: 4>
    __members__: typing.ClassVar[dict[str, EvalFlags]]  # value = {'None_': <EvalFlags.None_: 0>, 'IsScript': <EvalFlags.IsScript: 1>, 'CacheResults': <EvalFlags.CacheResults: 2>, 'SpecparamsAllowed': <EvalFlags.SpecparamsAllowed: 4>, 'CovergroupExpr': <EvalFlags.CovergroupExpr: 8>, 'AllowUnboundedPlaceholder': <EvalFlags.AllowUnboundedPlaceholder: 16>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EvaluatedDimension:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def associativeType(self) -> ...:
        ...
    @property
    def isRange(self) -> bool:
        ...
    @property
    def kind(self) -> DimensionKind:
        ...
    @property
    def queueMaxSize(self) -> int:
        ...
    @property
    def range(self) -> ...:
        ...
class EventControlSyntax(TimingControlSyntax):
    at: Token
    eventName: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EventControlWithExpressionSyntax(TimingControlSyntax):
    at: Token
    expr: EventExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EventExpressionSyntax(SequenceExprSyntax):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EventListControl(TimingControl):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def events(self) -> span[TimingControl]:
        ...
class EventTriggerStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def isNonBlocking(self) -> bool:
        ...
    @property
    def target(self) -> Expression:
        ...
    @property
    def timing(self) -> TimingControl:
        ...
class EventTriggerStatementSyntax(StatementSyntax):
    name: NameSyntax
    semi: Token
    timing: TimingControlSyntax
    trigger: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class EventType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExplicitAnsiPortSyntax(MemberSyntax):
    closeParen: Token
    direction: Token
    dot: Token
    expr: ExpressionSyntax
    name: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExplicitImportSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def importName(self) -> str:
        ...
    @property
    def importedSymbol(self) -> Symbol:
        ...
    @property
    def isFromExport(self) -> bool:
        ...
    @property
    def package(self) -> PackageSymbol:
        ...
    @property
    def packageName(self) -> str:
        ...
class ExplicitNonAnsiPortSyntax(NonAnsiPortSyntax):
    closeParen: Token
    dot: Token
    expr: PortExpressionSyntax
    name: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class Expression:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __repr__(self) -> str:
        ...
    def eval(self, context: EvalContext) -> ...:
        ...
    def evalLValue(self, context: EvalContext) -> LValue:
        ...
    def getSymbolReference(self, allowPacked: bool = True) -> ...:
        ...
    def isImplicitlyAssignableTo(self, compilation: Compilation, type: ...) -> bool:
        ...
    def visit(self, f: typing.Any) -> None:
        """
        Visit a pyslang object with a callback f.

        If f ever returns pyslang.VisitAction.Interrupt, the visit is aborted, and no additional nodes are visited. If f returns pyslang.VisitAction.Skip, then no child nodes of the current node are visited, but otherwise the visit continues. Any other return value, including pslang.VisitAction.Advance is ignored, and the walk continues.
        """
    @property
    def bad(self) -> bool:
        ...
    @property
    def constant(self) -> ...:
        ...
    @property
    def effectiveWidth(self) -> int | None:
        ...
    @property
    def hasHierarchicalReference(self) -> bool:
        ...
    @property
    def isImplicitString(self) -> bool:
        ...
    @property
    def isUnsizedInteger(self) -> bool:
        ...
    @property
    def kind(self) -> ExpressionKind:
        ...
    @property
    def sourceRange(self) -> ...:
        ...
    @property
    def syntax(self) -> ...:
        ...
    @property
    def type(self) -> ...:
        ...
class ExpressionConstraint(Constraint):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> ...:
        ...
    @property
    def isSoft(self) -> bool:
        ...
class ExpressionConstraintSyntax(ConstraintItemSyntax):
    expr: ExpressionSyntax
    semi: Token
    soft: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExpressionCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    expr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExpressionKind:
    """
    Members:

      Invalid

      IntegerLiteral

      RealLiteral

      TimeLiteral

      UnbasedUnsizedIntegerLiteral

      NullLiteral

      UnboundedLiteral

      StringLiteral

      NamedValue

      HierarchicalValue

      UnaryOp

      BinaryOp

      ConditionalOp

      Inside

      Assignment

      Concatenation

      Replication

      Streaming

      ElementSelect

      RangeSelect

      MemberAccess

      Call

      Conversion

      DataType

      TypeReference

      ArbitrarySymbol

      LValueReference

      SimpleAssignmentPattern

      StructuredAssignmentPattern

      ReplicatedAssignmentPattern

      EmptyArgument

      ValueRange

      Dist

      NewArray

      NewClass

      NewCovergroup

      CopyClass

      MinTypMax

      ClockingEvent

      AssertionInstance

      TaggedUnion
    """
    ArbitrarySymbol: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ArbitrarySymbol: 25>
    AssertionInstance: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.AssertionInstance: 39>
    Assignment: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Assignment: 14>
    BinaryOp: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.BinaryOp: 11>
    Call: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Call: 21>
    ClockingEvent: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ClockingEvent: 38>
    Concatenation: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Concatenation: 15>
    ConditionalOp: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ConditionalOp: 12>
    Conversion: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Conversion: 22>
    CopyClass: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.CopyClass: 36>
    DataType: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.DataType: 23>
    Dist: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Dist: 32>
    ElementSelect: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ElementSelect: 18>
    EmptyArgument: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.EmptyArgument: 30>
    HierarchicalValue: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.HierarchicalValue: 9>
    Inside: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Inside: 13>
    IntegerLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.IntegerLiteral: 1>
    Invalid: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Invalid: 0>
    LValueReference: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.LValueReference: 26>
    MemberAccess: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.MemberAccess: 20>
    MinTypMax: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.MinTypMax: 37>
    NamedValue: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.NamedValue: 8>
    NewArray: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.NewArray: 33>
    NewClass: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.NewClass: 34>
    NewCovergroup: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.NewCovergroup: 35>
    NullLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.NullLiteral: 5>
    RangeSelect: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.RangeSelect: 19>
    RealLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.RealLiteral: 2>
    ReplicatedAssignmentPattern: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ReplicatedAssignmentPattern: 29>
    Replication: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Replication: 16>
    SimpleAssignmentPattern: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.SimpleAssignmentPattern: 27>
    Streaming: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Streaming: 17>
    StringLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.StringLiteral: 7>
    StructuredAssignmentPattern: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.StructuredAssignmentPattern: 28>
    TaggedUnion: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.TaggedUnion: 40>
    TimeLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.TimeLiteral: 3>
    TypeReference: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.TypeReference: 24>
    UnaryOp: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.UnaryOp: 10>
    UnbasedUnsizedIntegerLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.UnbasedUnsizedIntegerLiteral: 4>
    UnboundedLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.UnboundedLiteral: 6>
    ValueRange: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ValueRange: 31>
    __members__: typing.ClassVar[dict[str, ExpressionKind]]  # value = {'Invalid': <ExpressionKind.Invalid: 0>, 'IntegerLiteral': <ExpressionKind.IntegerLiteral: 1>, 'RealLiteral': <ExpressionKind.RealLiteral: 2>, 'TimeLiteral': <ExpressionKind.TimeLiteral: 3>, 'UnbasedUnsizedIntegerLiteral': <ExpressionKind.UnbasedUnsizedIntegerLiteral: 4>, 'NullLiteral': <ExpressionKind.NullLiteral: 5>, 'UnboundedLiteral': <ExpressionKind.UnboundedLiteral: 6>, 'StringLiteral': <ExpressionKind.StringLiteral: 7>, 'NamedValue': <ExpressionKind.NamedValue: 8>, 'HierarchicalValue': <ExpressionKind.HierarchicalValue: 9>, 'UnaryOp': <ExpressionKind.UnaryOp: 10>, 'BinaryOp': <ExpressionKind.BinaryOp: 11>, 'ConditionalOp': <ExpressionKind.ConditionalOp: 12>, 'Inside': <ExpressionKind.Inside: 13>, 'Assignment': <ExpressionKind.Assignment: 14>, 'Concatenation': <ExpressionKind.Concatenation: 15>, 'Replication': <ExpressionKind.Replication: 16>, 'Streaming': <ExpressionKind.Streaming: 17>, 'ElementSelect': <ExpressionKind.ElementSelect: 18>, 'RangeSelect': <ExpressionKind.RangeSelect: 19>, 'MemberAccess': <ExpressionKind.MemberAccess: 20>, 'Call': <ExpressionKind.Call: 21>, 'Conversion': <ExpressionKind.Conversion: 22>, 'DataType': <ExpressionKind.DataType: 23>, 'TypeReference': <ExpressionKind.TypeReference: 24>, 'ArbitrarySymbol': <ExpressionKind.ArbitrarySymbol: 25>, 'LValueReference': <ExpressionKind.LValueReference: 26>, 'SimpleAssignmentPattern': <ExpressionKind.SimpleAssignmentPattern: 27>, 'StructuredAssignmentPattern': <ExpressionKind.StructuredAssignmentPattern: 28>, 'ReplicatedAssignmentPattern': <ExpressionKind.ReplicatedAssignmentPattern: 29>, 'EmptyArgument': <ExpressionKind.EmptyArgument: 30>, 'ValueRange': <ExpressionKind.ValueRange: 31>, 'Dist': <ExpressionKind.Dist: 32>, 'NewArray': <ExpressionKind.NewArray: 33>, 'NewClass': <ExpressionKind.NewClass: 34>, 'NewCovergroup': <ExpressionKind.NewCovergroup: 35>, 'CopyClass': <ExpressionKind.CopyClass: 36>, 'MinTypMax': <ExpressionKind.MinTypMax: 37>, 'ClockingEvent': <ExpressionKind.ClockingEvent: 38>, 'AssertionInstance': <ExpressionKind.AssertionInstance: 39>, 'TaggedUnion': <ExpressionKind.TaggedUnion: 40>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ExpressionOrDistSyntax(ExpressionSyntax):
    distribution: DistConstraintListSyntax
    expr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExpressionPatternSyntax(PatternSyntax):
    expr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExpressionStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> Expression:
        ...
class ExpressionStatementSyntax(StatementSyntax):
    expr: ExpressionSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExpressionSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExpressionTimingCheckArgSyntax(TimingCheckArgSyntax):
    expr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExtendsClauseSyntax(SyntaxNode):
    arguments: ArgumentListSyntax
    baseName: NameSyntax
    defaultedArg: DefaultExtendsClauseArgSyntax
    keyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExternInterfaceMethodSyntax(MemberSyntax):
    externKeyword: Token
    forkJoin: Token
    prototype: FunctionPrototypeSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExternModuleDeclSyntax(MemberSyntax):
    actualAttributes: ...
    externKeyword: Token
    header: ModuleHeaderSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ExternUdpDeclSyntax(MemberSyntax):
    actualAttributes: ...
    externKeyword: Token
    name: Token
    portList: UdpPortListSyntax
    primitive: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class FieldSymbol(VariableSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def bitOffset(self) -> int:
        ...
    @property
    def fieldIndex(self) -> int:
        ...
    @property
    def randMode(self) -> RandMode:
        ...
class FilePathSpecSyntax(SyntaxNode):
    path: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class FirstMatchAssertionExpr(AssertionExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def matchItems(self) -> span[...]:
        ...
    @property
    def seq(self) -> AssertionExpr:
        ...
class FirstMatchSequenceExprSyntax(SequenceExprSyntax):
    closeParen: Token
    expr: SequenceExprSyntax
    first_match: Token
    matchList: SequenceMatchListSyntax
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class FixedSizeUnpackedArrayType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def elementType(self) -> Type:
        ...
    @property
    def range(self) -> ConstantRange:
        ...
class FloatingType(Type):
    class Kind:
        """
        Members:

          Real

          ShortReal

          RealTime
        """
        Real: typing.ClassVar[FloatingType.Kind]  # value = <Kind.Real: 0>
        RealTime: typing.ClassVar[FloatingType.Kind]  # value = <Kind.RealTime: 2>
        ShortReal: typing.ClassVar[FloatingType.Kind]  # value = <Kind.ShortReal: 1>
        __members__: typing.ClassVar[dict[str, FloatingType.Kind]]  # value = {'Real': <Kind.Real: 0>, 'ShortReal': <Kind.ShortReal: 1>, 'RealTime': <Kind.RealTime: 2>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Real: typing.ClassVar[FloatingType.Kind]  # value = <Kind.Real: 0>
    RealTime: typing.ClassVar[FloatingType.Kind]  # value = <Kind.RealTime: 2>
    ShortReal: typing.ClassVar[FloatingType.Kind]  # value = <Kind.ShortReal: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def floatKind(self) -> ...:
        ...
class ForLoopStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def body(self) -> Statement:
        ...
    @property
    def initializers(self) -> span[Expression]:
        ...
    @property
    def loopVars(self) -> span[...]:
        ...
    @property
    def steps(self) -> span[Expression]:
        ...
    @property
    def stopExpr(self) -> Expression:
        ...
class ForLoopStatementSyntax(StatementSyntax):
    closeParen: Token
    forKeyword: Token
    initializers: ...
    openParen: Token
    semi1: Token
    semi2: Token
    statement: StatementSyntax
    steps: ...
    stopExpr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ForVariableDeclarationSyntax(SyntaxNode):
    declarator: DeclaratorSyntax
    type: DataTypeSyntax
    varKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ForeachConstraint(Constraint):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arrayRef(self) -> ...:
        ...
    @property
    def body(self) -> Constraint:
        ...
    @property
    def loopDims(self) -> span[...]:
        ...
class ForeachLoopListSyntax(SyntaxNode):
    arrayName: NameSyntax
    closeBracket: Token
    closeParen: Token
    loopVariables: ...
    openBracket: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ForeachLoopStatement(Statement):
    class LoopDim:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def loopVar(self) -> ...:
            ...
        @property
        def range(self) -> ConstantRange | None:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arrayRef(self) -> Expression:
        ...
    @property
    def body(self) -> Statement:
        ...
    @property
    def loopDims(self) -> span[...]:
        ...
class ForeachLoopStatementSyntax(StatementSyntax):
    keyword: Token
    loopList: ForeachLoopListSyntax
    statement: StatementSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ForeverLoopStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def body(self) -> Statement:
        ...
class ForeverStatementSyntax(StatementSyntax):
    foreverKeyword: Token
    statement: StatementSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class FormalArgumentSymbol(VariableSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def defaultValue(self) -> Expression:
        ...
    @property
    def direction(self) -> ArgumentDirection:
        ...
class ForwardTypeRestriction:
    """
    Members:

      None

      Enum

      Struct

      Union

      Class

      InterfaceClass
    """
    Class: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.Class: 4>
    Enum: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.Enum: 1>
    InterfaceClass: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.InterfaceClass: 5>
    None: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.None: 0>
    Struct: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.Struct: 2>
    Union: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.Union: 3>
    __members__: typing.ClassVar[dict[str, ForwardTypeRestriction]]  # value = {'None': <ForwardTypeRestriction.None: 0>, 'Enum': <ForwardTypeRestriction.Enum: 1>, 'Struct': <ForwardTypeRestriction.Struct: 2>, 'Union': <ForwardTypeRestriction.Union: 3>, 'Class': <ForwardTypeRestriction.Class: 4>, 'InterfaceClass': <ForwardTypeRestriction.InterfaceClass: 5>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ForwardTypeRestrictionSyntax(SyntaxNode):
    keyword1: Token
    keyword2: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ForwardTypedefDeclarationSyntax(MemberSyntax):
    name: Token
    semi: Token
    typeRestriction: ForwardTypeRestrictionSyntax
    typedefKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ForwardingTypedefSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def nextForwardDecl(self) -> ForwardingTypedefSymbol:
        ...
    @property
    def typeRestriction(self) -> ForwardTypeRestriction:
        ...
    @property
    def visibility(self) -> Visibility | None:
        ...
class FunctionDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    items: ...
    prototype: FunctionPrototypeSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class FunctionPortBaseSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class FunctionPortListSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    ports: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class FunctionPortSyntax(FunctionPortBaseSyntax):
    attributes: ...
    constKeyword: Token
    dataType: DataTypeSyntax
    declarator: DeclaratorSyntax
    direction: Token
    staticKeyword: Token
    varKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class FunctionPrototypeSyntax(SyntaxNode):
    keyword: Token
    lifetime: Token
    name: NameSyntax
    portList: FunctionPortListSyntax
    returnType: DataTypeSyntax
    specifiers: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class GenerateBlockArraySymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def constructIndex(self) -> int:
        ...
    @property
    def entries(self) -> span[GenerateBlockSymbol]:
        ...
    @property
    def externalName(self) -> str:
        ...
    @property
    def valid(self) -> bool:
        ...
class GenerateBlockSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arrayIndex(self) -> SVInt:
        ...
    @property
    def constructIndex(self) -> int:
        ...
    @property
    def externalName(self) -> str:
        ...
    @property
    def isUninstantiated(self) -> bool:
        ...
class GenerateBlockSyntax(MemberSyntax):
    begin: Token
    beginName: NamedBlockClauseSyntax
    end: Token
    endName: NamedBlockClauseSyntax
    label: NamedLabelSyntax
    members: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class GenerateRegionSyntax(MemberSyntax):
    endgenerate: Token
    keyword: Token
    members: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class GenericClassDefSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def defaultSpecialization(self) -> Type:
        ...
    @property
    def firstForwardDecl(self) -> ForwardingTypedefSymbol:
        ...
    @property
    def invalidSpecialization(self) -> Type:
        ...
    @property
    def isInterface(self) -> bool:
        ...
class GenvarDeclarationSyntax(MemberSyntax):
    identifiers: ...
    keyword: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class GenvarSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class HierarchicalInstanceSyntax(SyntaxNode):
    closeParen: Token
    connections: ...
    decl: InstanceNameSyntax
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class HierarchicalValueExpression(ValueExpressionBase):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class HierarchyInstantiationSyntax(MemberSyntax):
    instances: ...
    parameters: ParameterValueAssignmentSyntax
    semi: Token
    type: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class IdWithExprCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    id: Token
    withClause: WithClauseSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class IdentifierNameSyntax(NameSyntax):
    identifier: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class IdentifierSelectNameSyntax(NameSyntax):
    identifier: Token
    selectors: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class IfGenerateSyntax(MemberSyntax):
    block: MemberSyntax
    closeParen: Token
    condition: ExpressionSyntax
    elseClause: ElseClauseSyntax
    keyword: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class IfNonePathDeclarationSyntax(MemberSyntax):
    keyword: Token
    path: PathDeclarationSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class IffEventClauseSyntax(SyntaxNode):
    expr: ExpressionSyntax
    iff: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ImmediateAssertionMemberSyntax(MemberSyntax):
    statement: ImmediateAssertionStatementSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ImmediateAssertionStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def assertionKind(self) -> AssertionKind:
        ...
    @property
    def cond(self) -> Expression:
        ...
    @property
    def ifFalse(self) -> Statement:
        ...
    @property
    def ifTrue(self) -> Statement:
        ...
    @property
    def isDeferred(self) -> bool:
        ...
    @property
    def isFinal(self) -> bool:
        ...
class ImmediateAssertionStatementSyntax(StatementSyntax):
    action: ActionBlockSyntax
    delay: DeferredAssertionSyntax
    expr: ParenthesizedExpressionSyntax
    keyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ImplementsClauseSyntax(SyntaxNode):
    interfaces: ...
    keyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ImplicationConstraint(Constraint):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def body(self) -> Constraint:
        ...
    @property
    def predicate(self) -> ...:
        ...
class ImplicationConstraintSyntax(ConstraintItemSyntax):
    arrow: Token
    constraints: ConstraintItemSyntax
    left: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ImplicitAnsiPortSyntax(MemberSyntax):
    declarator: DeclaratorSyntax
    header: PortHeaderSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ImplicitEventControl(TimingControl):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ImplicitEventControlSyntax(TimingControlSyntax):
    at: Token
    closeParen: Token
    openParen: Token
    star: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ImplicitNonAnsiPortSyntax(NonAnsiPortSyntax):
    expr: PortExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ImplicitTypeSyntax(DataTypeSyntax):
    dimensions: ...
    placeholder: Token
    signing: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class IncludeDirectiveSyntax(DirectiveSyntax):
    fileName: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InsideExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def left(self) -> Expression:
        ...
    @property
    def rangeList(self) -> span[Expression]:
        ...
class InsideExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    inside: Token
    ranges: RangeListSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InstanceArraySymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arrayName(self) -> str:
        ...
    @property
    def elements(self) -> span[Symbol]:
        ...
    @property
    def range(self) -> ConstantRange:
        ...
class InstanceBodySymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def findPort(self, portName: str) -> Symbol:
        ...
    def hasSameType(self, other: InstanceBodySymbol) -> bool:
        ...
    @property
    def definition(self) -> DefinitionSymbol:
        ...
    @property
    def parameters(self) -> span[ParameterSymbolBase]:
        ...
    @property
    def parentInstance(self) -> InstanceSymbol:
        ...
    @property
    def portList(self) -> span[Symbol]:
        ...
class InstanceConfigRuleSyntax(ConfigRuleSyntax):
    instance: Token
    instanceNames: ...
    ruleClause: ConfigRuleClauseSyntax
    semi: Token
    topModule: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InstanceNameSyntax(SyntaxNode):
    dimensions: ...
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InstanceSymbol(InstanceSymbolBase):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def getPortConnection(self, port: PortSymbol) -> PortConnection:
        ...
    @typing.overload
    def getPortConnection(self, port: MultiPortSymbol) -> PortConnection:
        ...
    @typing.overload
    def getPortConnection(self, port: InterfacePortSymbol) -> PortConnection:
        ...
    @property
    def body(self) -> ...:
        ...
    @property
    def definition(self) -> DefinitionSymbol:
        ...
    @property
    def isInterface(self) -> bool:
        ...
    @property
    def isModule(self) -> bool:
        ...
    @property
    def portConnections(self) -> span[PortConnection]:
        ...
class InstanceSymbolBase(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arrayName(self) -> str:
        ...
    @property
    def arrayPath(self) -> span[int]:
        ...
class IntegerLiteral(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def isDeclaredUnsized(self) -> bool:
        ...
    @property
    def value(self) -> ...:
        ...
class IntegerTypeSyntax(DataTypeSyntax):
    dimensions: ...
    keyword: Token
    signing: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class IntegerVectorExpressionSyntax(PrimaryExpressionSyntax):
    base: Token
    size: Token
    value: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class IntegralFlags:
    """
    Members:

      Unsigned

      TwoState

      Signed

      FourState

      Reg
    """
    FourState: typing.ClassVar[IntegralFlags]  # value = <IntegralFlags.FourState: 2>
    Reg: typing.ClassVar[IntegralFlags]  # value = <IntegralFlags.Reg: 4>
    Signed: typing.ClassVar[IntegralFlags]  # value = <IntegralFlags.Signed: 1>
    TwoState: typing.ClassVar[IntegralFlags]  # value = <IntegralFlags.Unsigned: 0>
    Unsigned: typing.ClassVar[IntegralFlags]  # value = <IntegralFlags.Unsigned: 0>
    __members__: typing.ClassVar[dict[str, IntegralFlags]]  # value = {'Unsigned': <IntegralFlags.Unsigned: 0>, 'TwoState': <IntegralFlags.Unsigned: 0>, 'Signed': <IntegralFlags.Signed: 1>, 'FourState': <IntegralFlags.FourState: 2>, 'Reg': <IntegralFlags.Reg: 4>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IntegralType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def getBitVectorRange(self) -> ConstantRange:
        ...
    def isDeclaredReg(self) -> bool:
        ...
class InterfacePortHeaderSyntax(PortHeaderSyntax):
    modport: DotMemberClauseSyntax
    nameOrKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InterfacePortSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def connection(self) -> tuple[Symbol, ...]:
        ...
    @property
    def declaredRange(self) -> span[ConstantRange] | None:
        ...
    @property
    def interfaceDef(self) -> DefinitionSymbol:
        ...
    @property
    def isGeneric(self) -> bool:
        ...
    @property
    def isInvalid(self) -> bool:
        ...
    @property
    def modport(self) -> str:
        ...
class IntersectClauseSyntax(SyntaxNode):
    intersect: Token
    ranges: RangeListSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InvalidAssertionExpr(AssertionExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InvalidBinsSelectExpr(BinsSelectExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InvalidConstraint(Constraint):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InvalidExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InvalidPattern(Pattern):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InvalidStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InvalidTimingControl(TimingControl):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class InvocationExpressionSyntax(ExpressionSyntax):
    arguments: ArgumentListSyntax
    attributes: ...
    left: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class IteratorSymbol(TempVarSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class JumpStatementSyntax(StatementSyntax):
    breakOrContinue: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class KeywordNameSyntax(NameSyntax):
    keyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class KeywordTypeSyntax(DataTypeSyntax):
    keyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LValue:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def bad(self) -> bool:
        ...
    def load(self) -> ...:
        ...
    def resolve(self) -> ...:
        ...
    def store(self, value: ...) -> None:
        ...
class LValueReferenceExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LanguageVersion:
    """
    Members:

      v1800_2017

      v1800_2023

      Default
    """
    Default: typing.ClassVar[LanguageVersion]  # value = <LanguageVersion.v1800_2017: 0>
    __members__: typing.ClassVar[dict[str, LanguageVersion]]  # value = {'v1800_2017': <LanguageVersion.v1800_2017: 0>, 'v1800_2023': <LanguageVersion.v1800_2023: 1>, 'Default': <LanguageVersion.v1800_2017: 0>}
    v1800_2017: typing.ClassVar[LanguageVersion]  # value = <LanguageVersion.v1800_2017: 0>
    v1800_2023: typing.ClassVar[LanguageVersion]  # value = <LanguageVersion.v1800_2023: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LetDeclSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def ports(self) -> span[AssertionPortSymbol]:
        ...
class LetDeclarationSyntax(MemberSyntax):
    equals: Token
    expr: ExpressionSyntax
    identifier: Token
    let: Token
    portList: AssertionItemPortListSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LexerOptions:
    languageVersion: LanguageVersion
    maxErrors: int
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
class LibraryDeclarationSyntax(MemberSyntax):
    filePaths: ...
    incDirClause: LibraryIncDirClauseSyntax
    library: Token
    name: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LibraryIncDirClauseSyntax(SyntaxNode):
    filePaths: ...
    incdir: Token
    minus: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LibraryIncludeStatementSyntax(MemberSyntax):
    filePath: FilePathSpecSyntax
    include: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LibraryMapSyntax(SyntaxNode):
    endOfFile: Token
    members: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LineDirectiveSyntax(DirectiveSyntax):
    fileName: Token
    level: Token
    lineNumber: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LiteralBase:
    """
    Members:

      Binary

      Octal

      Decimal

      Hex
    """
    Binary: typing.ClassVar[LiteralBase]  # value = <LiteralBase.Binary: 0>
    Decimal: typing.ClassVar[LiteralBase]  # value = <LiteralBase.Decimal: 2>
    Hex: typing.ClassVar[LiteralBase]  # value = <LiteralBase.Hex: 3>
    Octal: typing.ClassVar[LiteralBase]  # value = <LiteralBase.Octal: 1>
    __members__: typing.ClassVar[dict[str, LiteralBase]]  # value = {'Binary': <LiteralBase.Binary: 0>, 'Octal': <LiteralBase.Octal: 1>, 'Decimal': <LiteralBase.Decimal: 2>, 'Hex': <LiteralBase.Hex: 3>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LiteralExpressionSyntax(PrimaryExpressionSyntax):
    literal: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LocalAssertionVarSymbol(VariableSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LocalVariableDeclarationSyntax(MemberSyntax):
    declarators: ...
    semi: Token
    type: DataTypeSyntax
    var: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class Lookup:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def ensureAccessible(symbol: ..., context: ASTContext, sourceRange: SourceRange | None) -> bool:
        ...
    @staticmethod
    def ensureVisible(symbol: ..., context: ASTContext, sourceRange: SourceRange | None) -> bool:
        ...
    @staticmethod
    def findAssertionLocalVar(context: ASTContext, name: ..., result: LookupResult) -> bool:
        ...
    @staticmethod
    def findClass(name: ..., context: ASTContext, requireInterfaceClass: DiagCode | None = None) -> ...:
        ...
    @staticmethod
    def findTempVar(scope: ..., symbol: ..., name: ..., result: LookupResult) -> bool:
        ...
    @staticmethod
    def getContainingClass(scope: ...) -> tuple[..., bool]:
        ...
    @staticmethod
    def getVisibility(symbol: ...) -> Visibility:
        ...
    @staticmethod
    def isAccessibleFrom(target: ..., sourceScope: ...) -> bool:
        ...
    @staticmethod
    def isVisibleFrom(symbol: ..., scope: ...) -> bool:
        ...
    @staticmethod
    def name(syntax: ..., context: ASTContext, flags: LookupFlags, result: LookupResult) -> None:
        ...
    @staticmethod
    def unqualified(scope: ..., name: str, flags: LookupFlags = ...) -> ...:
        ...
    @staticmethod
    def unqualifiedAt(scope: ..., name: str, location: LookupLocation, sourceRange: SourceRange, flags: LookupFlags = ...) -> ...:
        ...
    @staticmethod
    def withinClassRandomize(context: ASTContext, syntax: ..., flags: LookupFlags, result: LookupResult) -> bool:
        ...
class LookupFlags:
    """
    Members:

      None_

      Type

      AllowDeclaredAfter

      DisallowWildcardImport

      NoUndeclaredError

      NoUndeclaredErrorIfUninstantiated

      AllowIncompleteForwardTypedefs

      NoParentScope

      NoSelectors

      AllowRoot

      AllowUnit

      IfacePortConn

      StaticInitializer

      ForceHierarchical

      TypeReference

      AlwaysAllowUpward

      DisallowUnitReferences
    """
    AllowDeclaredAfter: typing.ClassVar[LookupFlags]  # value = <LookupFlags.AllowDeclaredAfter: 2>
    AllowIncompleteForwardTypedefs: typing.ClassVar[LookupFlags]  # value = <LookupFlags.AllowIncompleteForwardTypedefs: 32>
    AllowRoot: typing.ClassVar[LookupFlags]  # value = <LookupFlags.AllowRoot: 256>
    AllowUnit: typing.ClassVar[LookupFlags]  # value = <LookupFlags.AllowUnit: 512>
    AlwaysAllowUpward: typing.ClassVar[LookupFlags]  # value = <LookupFlags.AlwaysAllowUpward: 8192>
    DisallowUnitReferences: typing.ClassVar[LookupFlags]  # value = <LookupFlags.DisallowUnitReferences: 16384>
    DisallowWildcardImport: typing.ClassVar[LookupFlags]  # value = <LookupFlags.DisallowWildcardImport: 4>
    ForceHierarchical: typing.ClassVar[LookupFlags]  # value = <LookupFlags.ForceHierarchical: 18>
    IfacePortConn: typing.ClassVar[LookupFlags]  # value = <LookupFlags.IfacePortConn: 1024>
    NoParentScope: typing.ClassVar[LookupFlags]  # value = <LookupFlags.NoParentScope: 64>
    NoSelectors: typing.ClassVar[LookupFlags]  # value = <LookupFlags.NoSelectors: 128>
    NoUndeclaredError: typing.ClassVar[LookupFlags]  # value = <LookupFlags.NoUndeclaredError: 8>
    NoUndeclaredErrorIfUninstantiated: typing.ClassVar[LookupFlags]  # value = <LookupFlags.NoUndeclaredErrorIfUninstantiated: 16>
    None_: typing.ClassVar[LookupFlags]  # value = <LookupFlags.None_: 0>
    StaticInitializer: typing.ClassVar[LookupFlags]  # value = <LookupFlags.StaticInitializer: 2048>
    Type: typing.ClassVar[LookupFlags]  # value = <LookupFlags.Type: 1>
    TypeReference: typing.ClassVar[LookupFlags]  # value = <LookupFlags.TypeReference: 4096>
    __members__: typing.ClassVar[dict[str, LookupFlags]]  # value = {'None_': <LookupFlags.None_: 0>, 'Type': <LookupFlags.Type: 1>, 'AllowDeclaredAfter': <LookupFlags.AllowDeclaredAfter: 2>, 'DisallowWildcardImport': <LookupFlags.DisallowWildcardImport: 4>, 'NoUndeclaredError': <LookupFlags.NoUndeclaredError: 8>, 'NoUndeclaredErrorIfUninstantiated': <LookupFlags.NoUndeclaredErrorIfUninstantiated: 16>, 'AllowIncompleteForwardTypedefs': <LookupFlags.AllowIncompleteForwardTypedefs: 32>, 'NoParentScope': <LookupFlags.NoParentScope: 64>, 'NoSelectors': <LookupFlags.NoSelectors: 128>, 'AllowRoot': <LookupFlags.AllowRoot: 256>, 'AllowUnit': <LookupFlags.AllowUnit: 512>, 'IfacePortConn': <LookupFlags.IfacePortConn: 1024>, 'StaticInitializer': <LookupFlags.StaticInitializer: 2048>, 'ForceHierarchical': <LookupFlags.ForceHierarchical: 18>, 'TypeReference': <LookupFlags.TypeReference: 4096>, 'AlwaysAllowUpward': <LookupFlags.AlwaysAllowUpward: 8192>, 'DisallowUnitReferences': <LookupFlags.DisallowUnitReferences: 16384>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LookupLocation:
    __hash__: typing.ClassVar[None] = None
    max: typing.ClassVar[LookupLocation]  # value = <pyslang.LookupLocation object>
    min: typing.ClassVar[LookupLocation]  # value = <pyslang.LookupLocation object>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def after(symbol: ...) -> LookupLocation:
        ...
    @staticmethod
    def before(symbol: ...) -> LookupLocation:
        ...
    def __eq__(self, arg0: LookupLocation) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, scope: ..., index: int) -> None:
        ...
    def __ne__(self, arg0: LookupLocation) -> bool:
        ...
    @property
    def index(self) -> ...:
        ...
    @property
    def scope(self) -> ...:
        ...
class LookupResult:
    class MemberSelector:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def dotLocation(self) -> SourceLocation:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def nameRange(self) -> SourceRange:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def clear(self) -> None:
        ...
    def errorIfSelectors(self, context: ASTContext) -> None:
        ...
    def reportDiags(self, context: ASTContext) -> None:
        ...
    @property
    def diagnostics(self) -> Diagnostics:
        ...
    @property
    def flags(self) -> LookupResultFlags:
        ...
    @property
    def found(self) -> ...:
        ...
    @property
    def hasError(self) -> bool:
        ...
    @property
    def selectors(self) -> ...:
        ...
    @property
    def systemSubroutine(self) -> SystemSubroutine:
        ...
    @property
    def upwardCount(self) -> int:
        ...
class LookupResultFlags:
    """
    Members:

      None_

      WasImported

      IsHierarchical

      SuppressUndeclared

      FromTypeParam

      FromForwardTypedef
    """
    FromForwardTypedef: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.FromForwardTypedef: 16>
    FromTypeParam: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.FromTypeParam: 8>
    IsHierarchical: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.IsHierarchical: 2>
    None_: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.None_: 0>
    SuppressUndeclared: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.SuppressUndeclared: 4>
    WasImported: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.WasImported: 1>
    __members__: typing.ClassVar[dict[str, LookupResultFlags]]  # value = {'None_': <LookupResultFlags.None_: 0>, 'WasImported': <LookupResultFlags.WasImported: 1>, 'IsHierarchical': <LookupResultFlags.IsHierarchical: 2>, 'SuppressUndeclared': <LookupResultFlags.SuppressUndeclared: 4>, 'FromTypeParam': <LookupResultFlags.FromTypeParam: 8>, 'FromForwardTypedef': <LookupResultFlags.FromForwardTypedef: 16>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LoopConstraintSyntax(ConstraintItemSyntax):
    constraints: ConstraintItemSyntax
    foreachKeyword: Token
    loopList: ForeachLoopListSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LoopGenerateSyntax(MemberSyntax):
    block: MemberSyntax
    closeParen: Token
    equals: Token
    genvar: Token
    identifier: Token
    initialExpr: ExpressionSyntax
    iterationExpr: ExpressionSyntax
    keyword: Token
    openParen: Token
    semi1: Token
    semi2: Token
    stopExpr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class LoopStatementSyntax(StatementSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    repeatOrWhile: Token
    statement: StatementSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class MacroActualArgumentListSyntax(SyntaxNode):
    args: ...
    closeParen: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class MacroActualArgumentSyntax(SyntaxNode):
    tokens: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class MacroArgumentDefaultSyntax(SyntaxNode):
    equals: Token
    tokens: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class MacroFormalArgumentListSyntax(SyntaxNode):
    args: ...
    closeParen: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class MacroFormalArgumentSyntax(SyntaxNode):
    defaultValue: MacroArgumentDefaultSyntax
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class MacroUsageSyntax(DirectiveSyntax):
    args: MacroActualArgumentListSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class MatchesClauseSyntax(SyntaxNode):
    matchesKeyword: Token
    pattern: PatternSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class MemberAccessExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def member(self) -> ...:
        ...
    @property
    def value(self) -> Expression:
        ...
class MemberAccessExpressionSyntax(ExpressionSyntax):
    dot: Token
    left: ExpressionSyntax
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class MemberSyntax(SyntaxNode):
    attributes: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class MethodFlags:
    """
    Members:

      None_

      Virtual

      Pure

      Static

      Constructor

      InterfaceExtern

      ModportImport

      ModportExport

      DPIImport

      DPIContext

      BuiltIn

      Randomize

      ForkJoin

      DefaultedSuperArg

      Initial

      Extends

      Final
    """
    BuiltIn: typing.ClassVar[MethodFlags]  # value = <MethodFlags.BuiltIn: 512>
    Constructor: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Constructor: 8>
    DPIContext: typing.ClassVar[MethodFlags]  # value = <MethodFlags.DPIContext: 256>
    DPIImport: typing.ClassVar[MethodFlags]  # value = <MethodFlags.DPIImport: 128>
    DefaultedSuperArg: typing.ClassVar[MethodFlags]  # value = <MethodFlags.DefaultedSuperArg: 4096>
    Extends: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Extends: 16384>
    Final: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Final: 32768>
    ForkJoin: typing.ClassVar[MethodFlags]  # value = <MethodFlags.ForkJoin: 2048>
    Initial: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Initial: 8192>
    InterfaceExtern: typing.ClassVar[MethodFlags]  # value = <MethodFlags.InterfaceExtern: 16>
    ModportExport: typing.ClassVar[MethodFlags]  # value = <MethodFlags.ModportExport: 64>
    ModportImport: typing.ClassVar[MethodFlags]  # value = <MethodFlags.ModportImport: 32>
    None_: typing.ClassVar[MethodFlags]  # value = <MethodFlags.None_: 0>
    Pure: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Pure: 2>
    Randomize: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Randomize: 1024>
    Static: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Static: 4>
    Virtual: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Virtual: 1>
    __members__: typing.ClassVar[dict[str, MethodFlags]]  # value = {'None_': <MethodFlags.None_: 0>, 'Virtual': <MethodFlags.Virtual: 1>, 'Pure': <MethodFlags.Pure: 2>, 'Static': <MethodFlags.Static: 4>, 'Constructor': <MethodFlags.Constructor: 8>, 'InterfaceExtern': <MethodFlags.InterfaceExtern: 16>, 'ModportImport': <MethodFlags.ModportImport: 32>, 'ModportExport': <MethodFlags.ModportExport: 64>, 'DPIImport': <MethodFlags.DPIImport: 128>, 'DPIContext': <MethodFlags.DPIContext: 256>, 'BuiltIn': <MethodFlags.BuiltIn: 512>, 'Randomize': <MethodFlags.Randomize: 1024>, 'ForkJoin': <MethodFlags.ForkJoin: 2048>, 'DefaultedSuperArg': <MethodFlags.DefaultedSuperArg: 4096>, 'Initial': <MethodFlags.Initial: 8192>, 'Extends': <MethodFlags.Extends: 16384>, 'Final': <MethodFlags.Final: 32768>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MethodPrototypeSymbol(Symbol, Scope):
    class ExternImpl:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def impl(self) -> SubroutineSymbol:
            ...
        @property
        def nextImpl(self) -> MethodPrototypeSymbol.ExternImpl:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arguments(self) -> span[FormalArgumentSymbol]:
        ...
    @property
    def firstExternImpl(self) -> ...:
        ...
    @property
    def flags(self) -> MethodFlags:
        ...
    @property
    def isVirtual(self) -> bool:
        ...
    @property
    def override(self) -> Symbol:
        ...
    @property
    def returnType(self) -> ...:
        ...
    @property
    def subroutine(self) -> SubroutineSymbol:
        ...
    @property
    def subroutineKind(self) -> SubroutineKind:
        ...
    @property
    def visibility(self) -> Visibility:
        ...
class MinTypMax:
    """
    Members:

      Min

      Typ

      Max
    """
    Max: typing.ClassVar[MinTypMax]  # value = <MinTypMax.Max: 2>
    Min: typing.ClassVar[MinTypMax]  # value = <MinTypMax.Min: 0>
    Typ: typing.ClassVar[MinTypMax]  # value = <MinTypMax.Typ: 1>
    __members__: typing.ClassVar[dict[str, MinTypMax]]  # value = {'Min': <MinTypMax.Min: 0>, 'Typ': <MinTypMax.Typ: 1>, 'Max': <MinTypMax.Max: 2>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MinTypMaxExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def max(self) -> Expression:
        ...
    @property
    def min(self) -> Expression:
        ...
    @property
    def selected(self) -> Expression:
        ...
    @property
    def typ(self) -> Expression:
        ...
class MinTypMaxExpressionSyntax(ExpressionSyntax):
    colon1: Token
    colon2: Token
    max: ExpressionSyntax
    min: ExpressionSyntax
    typ: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ModportClockingPortSyntax(MemberSyntax):
    clocking: Token
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ModportClockingSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def target(self) -> Symbol:
        ...
class ModportDeclarationSyntax(MemberSyntax):
    items: ...
    keyword: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ModportExplicitPortSyntax(ModportPortSyntax):
    closeParen: Token
    dot: Token
    expr: ExpressionSyntax
    name: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ModportItemSyntax(SyntaxNode):
    name: Token
    ports: AnsiPortListSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ModportNamedPortSyntax(ModportPortSyntax):
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ModportPortSymbol(ValueSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def direction(self) -> ArgumentDirection:
        ...
    @property
    def explicitConnection(self) -> Expression:
        ...
    @property
    def internalSymbol(self) -> Symbol:
        ...
class ModportPortSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ModportSimplePortListSyntax(MemberSyntax):
    direction: Token
    ports: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ModportSubroutinePortListSyntax(MemberSyntax):
    importExport: Token
    ports: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ModportSubroutinePortSyntax(ModportPortSyntax):
    prototype: FunctionPrototypeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ModportSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def hasExports(self) -> bool:
        ...
class ModuleDeclarationSyntax(MemberSyntax):
    blockName: NamedBlockClauseSyntax
    endmodule: Token
    header: ModuleHeaderSyntax
    members: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ModuleHeaderSyntax(SyntaxNode):
    imports: ...
    lifetime: Token
    moduleKeyword: Token
    name: Token
    parameters: ParameterPortListSyntax
    ports: PortListSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class MultiPortSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def direction(self) -> ArgumentDirection:
        ...
    @property
    def initializer(self) -> Expression:
        ...
    @property
    def isNullPort(self) -> bool:
        ...
    @property
    def ports(self) -> span[PortSymbol]:
        ...
    @property
    def type(self) -> ...:
        ...
class MultipleConcatenationExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    concatenation: ConcatenationExpressionSyntax
    expression: ExpressionSyntax
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NameSyntax(ExpressionSyntax):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NameValuePragmaExpressionSyntax(PragmaExpressionSyntax):
    equals: Token
    name: Token
    value: PragmaExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NamedArgumentSyntax(ArgumentSyntax):
    closeParen: Token
    dot: Token
    expr: PropertyExprSyntax
    name: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NamedBlockClauseSyntax(SyntaxNode):
    colon: Token
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NamedConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NamedLabelSyntax(SyntaxNode):
    colon: Token
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NamedParamAssignmentSyntax(ParamAssignmentSyntax):
    closeParen: Token
    dot: Token
    expr: ExpressionSyntax
    name: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NamedPortConnectionSyntax(PortConnectionSyntax):
    closeParen: Token
    dot: Token
    expr: PropertyExprSyntax
    name: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NamedStructurePatternMemberSyntax(StructurePatternMemberSyntax):
    colon: Token
    name: Token
    pattern: PatternSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NamedTypeSyntax(DataTypeSyntax):
    name: NameSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NamedValueExpression(ValueExpressionBase):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NetAliasSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def netReferences(self) -> span[Expression]:
        ...
class NetAliasSyntax(MemberSyntax):
    keyword: Token
    nets: ...
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NetDeclarationSyntax(MemberSyntax):
    declarators: ...
    delay: TimingControlSyntax
    expansionHint: Token
    netType: Token
    semi: Token
    strength: NetStrengthSyntax
    type: DataTypeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NetPortHeaderSyntax(PortHeaderSyntax):
    dataType: DataTypeSyntax
    direction: Token
    netType: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NetStrengthSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NetSymbol(ValueSymbol):
    class ExpansionHint:
        """
        Members:

          None_

          Vectored

          Scalared
        """
        None_: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.None_: 0>
        Scalared: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.Scalared: 2>
        Vectored: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.Vectored: 1>
        __members__: typing.ClassVar[dict[str, NetSymbol.ExpansionHint]]  # value = {'None_': <ExpansionHint.None_: 0>, 'Vectored': <ExpansionHint.Vectored: 1>, 'Scalared': <ExpansionHint.Scalared: 2>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    None_: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.None_: 0>
    Scalared: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.Scalared: 2>
    Vectored: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.Vectored: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def chargeStrength(self) -> ... | None:
        ...
    @property
    def delay(self) -> TimingControl:
        ...
    @property
    def driveStrength(self) -> tuple[... | None, ... | None]:
        ...
    @property
    def expansionHint(self) -> ...:
        ...
    @property
    def isImplicit(self) -> bool:
        ...
    @property
    def netType(self) -> ...:
        ...
class NetType(Symbol):
    class NetKind:
        """
        Members:

          Unknown

          Wire

          WAnd

          WOr

          Tri

          TriAnd

          TriOr

          Tri0

          Tri1

          TriReg

          Supply0

          Supply1

          UWire

          Interconnect

          UserDefined
        """
        Interconnect: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Interconnect: 13>
        Supply0: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Supply0: 10>
        Supply1: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Supply1: 11>
        Tri: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri: 4>
        Tri0: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri0: 7>
        Tri1: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri1: 8>
        TriAnd: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriAnd: 5>
        TriOr: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriOr: 6>
        TriReg: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriReg: 9>
        UWire: typing.ClassVar[NetType.NetKind]  # value = <NetKind.UWire: 12>
        Unknown: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Unknown: 0>
        UserDefined: typing.ClassVar[NetType.NetKind]  # value = <NetKind.UserDefined: 14>
        WAnd: typing.ClassVar[NetType.NetKind]  # value = <NetKind.WAnd: 2>
        WOr: typing.ClassVar[NetType.NetKind]  # value = <NetKind.WOr: 3>
        Wire: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Wire: 1>
        __members__: typing.ClassVar[dict[str, NetType.NetKind]]  # value = {'Unknown': <NetKind.Unknown: 0>, 'Wire': <NetKind.Wire: 1>, 'WAnd': <NetKind.WAnd: 2>, 'WOr': <NetKind.WOr: 3>, 'Tri': <NetKind.Tri: 4>, 'TriAnd': <NetKind.TriAnd: 5>, 'TriOr': <NetKind.TriOr: 6>, 'Tri0': <NetKind.Tri0: 7>, 'Tri1': <NetKind.Tri1: 8>, 'TriReg': <NetKind.TriReg: 9>, 'Supply0': <NetKind.Supply0: 10>, 'Supply1': <NetKind.Supply1: 11>, 'UWire': <NetKind.UWire: 12>, 'Interconnect': <NetKind.Interconnect: 13>, 'UserDefined': <NetKind.UserDefined: 14>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Interconnect: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Interconnect: 13>
    Supply0: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Supply0: 10>
    Supply1: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Supply1: 11>
    Tri: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri: 4>
    Tri0: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri0: 7>
    Tri1: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri1: 8>
    TriAnd: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriAnd: 5>
    TriOr: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriOr: 6>
    TriReg: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriReg: 9>
    UWire: typing.ClassVar[NetType.NetKind]  # value = <NetKind.UWire: 12>
    Unknown: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Unknown: 0>
    UserDefined: typing.ClassVar[NetType.NetKind]  # value = <NetKind.UserDefined: 14>
    WAnd: typing.ClassVar[NetType.NetKind]  # value = <NetKind.WAnd: 2>
    WOr: typing.ClassVar[NetType.NetKind]  # value = <NetKind.WOr: 3>
    Wire: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Wire: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def getSimulatedNetType(internal: NetType, external: NetType, shouldWarn: bool) -> NetType:
        ...
    @property
    def declaredType(self) -> ...:
        ...
    @property
    def isBuiltIn(self) -> bool:
        ...
    @property
    def isError(self) -> bool:
        ...
    @property
    def netKind(self) -> ...:
        ...
    @property
    def resolutionFunction(self) -> SubroutineSymbol:
        ...
class NetTypeDeclarationSyntax(MemberSyntax):
    keyword: Token
    name: Token
    semi: Token
    type: DataTypeSyntax
    withFunction: WithFunctionClauseSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NewArrayExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def initExpr(self) -> Expression:
        ...
    @property
    def sizeExpr(self) -> Expression:
        ...
class NewArrayExpressionSyntax(ExpressionSyntax):
    closeBracket: Token
    initializer: ParenthesizedExpressionSyntax
    newKeyword: NameSyntax
    openBracket: Token
    sizeExpr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NewClassExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def constructorCall(self) -> Expression:
        ...
    @property
    def isSuperClass(self) -> bool:
        ...
class NewClassExpressionSyntax(ExpressionSyntax):
    argList: ArgumentListSyntax
    scopedNew: NameSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NewCovergroupExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arguments(self) -> span[Expression]:
        ...
class NonAnsiPortListSyntax(PortListSyntax):
    closeParen: Token
    openParen: Token
    ports: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NonAnsiPortSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NonAnsiUdpPortListSyntax(UdpPortListSyntax):
    closeParen: Token
    openParen: Token
    ports: ...
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NonConstantFunction(SimpleSystemSubroutine):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, name: str, returnType: ..., requiredArgs: int = 0, argTypes: list[...] = [], isMethod: bool = False) -> None:
        ...
class Null:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class NullLiteral(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NullType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class NumberPragmaExpressionSyntax(PragmaExpressionSyntax):
    base: Token
    size: Token
    value: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class OneStepDelayControl(TimingControl):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class OneStepDelaySyntax(TimingControlSyntax):
    hash: Token
    oneStep: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class OrderedArgumentSyntax(ArgumentSyntax):
    expr: PropertyExprSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class OrderedParamAssignmentSyntax(ParamAssignmentSyntax):
    expr: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class OrderedPortConnectionSyntax(PortConnectionSyntax):
    expr: PropertyExprSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class OrderedStructurePatternMemberSyntax(StructurePatternMemberSyntax):
    pattern: PatternSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PackageExportAllDeclarationSyntax(MemberSyntax):
    doubleColon: Token
    keyword: Token
    semi: Token
    star1: Token
    star2: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PackageExportDeclarationSyntax(MemberSyntax):
    items: ...
    keyword: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PackageImportDeclarationSyntax(MemberSyntax):
    items: ...
    keyword: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PackageImportItemSyntax(SyntaxNode):
    doubleColon: Token
    item: Token
    package: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PackageSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def findForImport(self, name: str) -> Symbol:
        ...
    @property
    def defaultLifetime(self) -> VariableLifetime:
        ...
    @property
    def defaultNetType(self) -> ...:
        ...
    @property
    def exportDecls(self) -> span[...]:
        ...
    @property
    def hasExportAll(self) -> bool:
        ...
    @property
    def timeScale(self) -> TimeScale | None:
        ...
class PackedArrayType(IntegralType):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def elementType(self) -> Type:
        ...
    @property
    def range(self) -> ConstantRange:
        ...
class PackedStructType(IntegralType, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def systemId(self) -> int:
        ...
class PackedUnionType(IntegralType, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def isSoft(self) -> bool:
        ...
    @property
    def isTagged(self) -> bool:
        ...
    @property
    def systemId(self) -> int:
        ...
    @property
    def tagBits(self) -> int:
        ...
class ParamAssignmentSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParameterDeclarationBaseSyntax(SyntaxNode):
    keyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParameterDeclarationStatementSyntax(MemberSyntax):
    parameter: ParameterDeclarationBaseSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParameterDeclarationSyntax(ParameterDeclarationBaseSyntax):
    declarators: ...
    type: DataTypeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParameterPortListSyntax(SyntaxNode):
    closeParen: Token
    declarations: ...
    hash: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParameterSymbol(ValueSymbol, ParameterSymbolBase):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def isOverridden(self) -> bool:
        ...
    @property
    def value(self) -> ConstantValue:
        ...
class ParameterSymbolBase:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def isBodyParam(self) -> bool:
        ...
    @property
    def isLocalParam(self) -> bool:
        ...
    @property
    def isPortParam(self) -> bool:
        ...
class ParameterValueAssignmentSyntax(SyntaxNode):
    closeParen: Token
    hash: Token
    openParen: Token
    parameters: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParenExpressionListSyntax(SyntaxNode):
    closeParen: Token
    expressions: ...
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParenPragmaExpressionSyntax(PragmaExpressionSyntax):
    closeParen: Token
    openParen: Token
    values: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParenthesizedBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    closeParen: Token
    expr: BinsSelectExpressionSyntax
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParenthesizedConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    closeParen: Token
    openParen: Token
    operand: ConditionalDirectiveExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParenthesizedEventExpressionSyntax(EventExpressionSyntax):
    closeParen: Token
    expr: EventExpressionSyntax
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParenthesizedExpressionSyntax(PrimaryExpressionSyntax):
    closeParen: Token
    expression: ExpressionSyntax
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParenthesizedPatternSyntax(PatternSyntax):
    closeParen: Token
    openParen: Token
    pattern: PatternSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParenthesizedPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    expr: PropertyExprSyntax
    matchList: SequenceMatchListSyntax
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParenthesizedSequenceExprSyntax(SequenceExprSyntax):
    closeParen: Token
    expr: SequenceExprSyntax
    matchList: SequenceMatchListSyntax
    openParen: Token
    repetition: SequenceRepetitionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ParserOptions:
    languageVersion: LanguageVersion
    maxRecursionDepth: int
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
class PathDeclarationSyntax(MemberSyntax):
    closeParen: Token
    delays: ...
    desc: PathDescriptionSyntax
    equals: Token
    openParen: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PathDescriptionSyntax(SyntaxNode):
    closeParen: Token
    edgeIdentifier: Token
    inputs: ...
    openParen: Token
    pathOperator: Token
    polarityOperator: Token
    suffix: PathSuffixSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PathSuffixSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class Pattern:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __repr__(self) -> str:
        ...
    def eval(self, context: EvalContext, value: ..., conditionKind: ...) -> ...:
        ...
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> PatternKind:
        ...
    @property
    def sourceRange(self) -> ...:
        ...
    @property
    def syntax(self) -> ...:
        ...
class PatternCaseItemSyntax(CaseItemSyntax):
    colon: Token
    expr: ExpressionSyntax
    pattern: PatternSyntax
    statement: StatementSyntax
    tripleAnd: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PatternCaseStatement(Statement):
    class ItemGroup:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def filter(self) -> Expression:
            ...
        @property
        def pattern(self) -> Pattern:
            ...
        @property
        def stmt(self) -> Statement:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def check(self) -> UniquePriorityCheck:
        ...
    @property
    def condition(self) -> CaseStatementCondition:
        ...
    @property
    def defaultCase(self) -> Statement:
        ...
    @property
    def expr(self) -> Expression:
        ...
    @property
    def items(self) -> span[...]:
        ...
class PatternKind:
    """
    Members:

      Invalid

      Wildcard

      Constant

      Variable

      Tagged

      Structure
    """
    Constant: typing.ClassVar[PatternKind]  # value = <PatternKind.Constant: 2>
    Invalid: typing.ClassVar[PatternKind]  # value = <PatternKind.Invalid: 0>
    Structure: typing.ClassVar[PatternKind]  # value = <PatternKind.Structure: 5>
    Tagged: typing.ClassVar[PatternKind]  # value = <PatternKind.Tagged: 4>
    Variable: typing.ClassVar[PatternKind]  # value = <PatternKind.Variable: 3>
    Wildcard: typing.ClassVar[PatternKind]  # value = <PatternKind.Wildcard: 1>
    __members__: typing.ClassVar[dict[str, PatternKind]]  # value = {'Invalid': <PatternKind.Invalid: 0>, 'Wildcard': <PatternKind.Wildcard: 1>, 'Constant': <PatternKind.Constant: 2>, 'Variable': <PatternKind.Variable: 3>, 'Tagged': <PatternKind.Tagged: 4>, 'Structure': <PatternKind.Structure: 5>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PatternSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PatternVarSymbol(TempVarSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PortConcatenationSyntax(PortExpressionSyntax):
    closeBrace: Token
    openBrace: Token
    references: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PortConnection:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expression(self) -> Expression:
        ...
    @property
    def ifaceConn(self) -> tuple[Symbol, ...]:
        ...
    @property
    def port(self) -> Symbol:
        ...
class PortConnectionSyntax(SyntaxNode):
    attributes: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PortDeclarationSyntax(MemberSyntax):
    declarators: ...
    header: PortHeaderSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PortExpressionSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PortHeaderSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PortListSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PortReferenceSyntax(PortExpressionSyntax):
    name: Token
    select: ElementSelectSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PortSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def direction(self) -> ArgumentDirection:
        ...
    @property
    def externalLoc(self) -> SourceLocation:
        ...
    @property
    def initializer(self) -> Expression:
        ...
    @property
    def internalExpr(self) -> Expression:
        ...
    @property
    def internalSymbol(self) -> Symbol:
        ...
    @property
    def isAnsiPort(self) -> bool:
        ...
    @property
    def isNetPort(self) -> bool:
        ...
    @property
    def isNullPort(self) -> bool:
        ...
    @property
    def type(self) -> ...:
        ...
class PostfixUnaryExpressionSyntax(ExpressionSyntax):
    attributes: ...
    operand: ExpressionSyntax
    operatorToken: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PragmaDirectiveSyntax(DirectiveSyntax):
    args: ...
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PragmaExpressionSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PredefinedIntegerType(IntegralType):
    class Kind:
        """
        Members:

          ShortInt

          Int

          LongInt

          Byte

          Integer

          Time
        """
        Byte: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Byte: 3>
        Int: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Int: 1>
        Integer: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Integer: 4>
        LongInt: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.LongInt: 2>
        ShortInt: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.ShortInt: 0>
        Time: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Time: 5>
        __members__: typing.ClassVar[dict[str, PredefinedIntegerType.Kind]]  # value = {'ShortInt': <Kind.ShortInt: 0>, 'Int': <Kind.Int: 1>, 'LongInt': <Kind.LongInt: 2>, 'Byte': <Kind.Byte: 3>, 'Integer': <Kind.Integer: 4>, 'Time': <Kind.Time: 5>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Byte: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Byte: 3>
    Int: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Int: 1>
    Integer: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Integer: 4>
    LongInt: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.LongInt: 2>
    ShortInt: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.ShortInt: 0>
    Time: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Time: 5>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def integerKind(self) -> ...:
        ...
class PrefixUnaryExpressionSyntax(ExpressionSyntax):
    attributes: ...
    operand: ExpressionSyntax
    operatorToken: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PreprocessorOptions:
    additionalIncludePaths: list[os.PathLike]
    ignoreDirectives: set[str]
    languageVersion: LanguageVersion
    maxIncludeDepth: int
    predefineSource: str
    predefines: list[str]
    undefines: list[str]
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
class PrimaryBlockEventExpressionSyntax(BlockEventExpressionSyntax):
    keyword: Token
    name: NameSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PrimaryExpressionSyntax(ExpressionSyntax):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PrimitiveInstanceSymbol(InstanceSymbolBase):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def delay(self) -> TimingControl:
        ...
    @property
    def driveStrength(self) -> tuple[... | None, ... | None]:
        ...
    @property
    def portConnections(self) -> span[Expression]:
        ...
    @property
    def primitiveType(self) -> ...:
        ...
class PrimitiveInstantiationSyntax(MemberSyntax):
    delay: TimingControlSyntax
    instances: ...
    semi: Token
    strength: NetStrengthSyntax
    type: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PrimitivePortDirection:
    """
    Members:

      In

      Out

      OutReg

      InOut
    """
    In: typing.ClassVar[PrimitivePortDirection]  # value = <PrimitivePortDirection.In: 0>
    InOut: typing.ClassVar[PrimitivePortDirection]  # value = <PrimitivePortDirection.InOut: 3>
    Out: typing.ClassVar[PrimitivePortDirection]  # value = <PrimitivePortDirection.Out: 1>
    OutReg: typing.ClassVar[PrimitivePortDirection]  # value = <PrimitivePortDirection.OutReg: 2>
    __members__: typing.ClassVar[dict[str, PrimitivePortDirection]]  # value = {'In': <PrimitivePortDirection.In: 0>, 'Out': <PrimitivePortDirection.Out: 1>, 'OutReg': <PrimitivePortDirection.OutReg: 2>, 'InOut': <PrimitivePortDirection.InOut: 3>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PrimitivePortSymbol(ValueSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def direction(self) -> PrimitivePortDirection:
        ...
class PrimitiveSymbol(Symbol, Scope):
    class PrimitiveKind:
        """
        Members:

          UserDefined

          Fixed

          NInput

          NOutput
        """
        Fixed: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.Fixed: 1>
        NInput: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.NInput: 2>
        NOutput: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.NOutput: 3>
        UserDefined: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.UserDefined: 0>
        __members__: typing.ClassVar[dict[str, PrimitiveSymbol.PrimitiveKind]]  # value = {'UserDefined': <PrimitiveKind.UserDefined: 0>, 'Fixed': <PrimitiveKind.Fixed: 1>, 'NInput': <PrimitiveKind.NInput: 2>, 'NOutput': <PrimitiveKind.NOutput: 3>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class TableEntry:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def inputs(self) -> str:
            ...
        @property
        def output(self) -> str:
            ...
        @property
        def state(self) -> str:
            ...
    Fixed: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.Fixed: 1>
    NInput: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.NInput: 2>
    NOutput: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.NOutput: 3>
    UserDefined: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.UserDefined: 0>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def initVal(self) -> ConstantValue:
        ...
    @property
    def isSequential(self) -> bool:
        ...
    @property
    def ports(self) -> span[PrimitivePortSymbol]:
        ...
    @property
    def primitiveKind(self) -> ...:
        ...
    @property
    def table(self) -> span[...]:
        ...
class ProceduralAssignStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def assignment(self) -> Expression:
        ...
    @property
    def isForce(self) -> bool:
        ...
class ProceduralAssignStatementSyntax(StatementSyntax):
    expr: ExpressionSyntax
    keyword: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ProceduralBlockKind:
    """
    Members:

      Initial

      Final

      Always

      AlwaysComb

      AlwaysLatch

      AlwaysFF
    """
    Always: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.Always: 2>
    AlwaysComb: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.AlwaysComb: 3>
    AlwaysFF: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.AlwaysFF: 5>
    AlwaysLatch: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.AlwaysLatch: 4>
    Final: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.Final: 1>
    Initial: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.Initial: 0>
    __members__: typing.ClassVar[dict[str, ProceduralBlockKind]]  # value = {'Initial': <ProceduralBlockKind.Initial: 0>, 'Final': <ProceduralBlockKind.Final: 1>, 'Always': <ProceduralBlockKind.Always: 2>, 'AlwaysComb': <ProceduralBlockKind.AlwaysComb: 3>, 'AlwaysLatch': <ProceduralBlockKind.AlwaysLatch: 4>, 'AlwaysFF': <ProceduralBlockKind.AlwaysFF: 5>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ProceduralBlockSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def body(self) -> Statement:
        ...
    @property
    def isSingleDriverBlock(self) -> bool:
        ...
    @property
    def procedureKind(self) -> ProceduralBlockKind:
        ...
class ProceduralBlockSyntax(MemberSyntax):
    keyword: Token
    statement: StatementSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ProceduralCheckerStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def instances(self) -> span[...]:
        ...
class ProceduralDeassignStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def isRelease(self) -> bool:
        ...
    @property
    def lvalue(self) -> Expression:
        ...
class ProceduralDeassignStatementSyntax(StatementSyntax):
    keyword: Token
    semi: Token
    variable: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ProductionSyntax(SyntaxNode):
    colon: Token
    dataType: DataTypeSyntax
    name: Token
    portList: FunctionPortListSyntax
    rules: ...
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PropertyCaseItemSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PropertyDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    keyword: Token
    name: Token
    optionalSemi: Token
    portList: AssertionItemPortListSyntax
    propertySpec: PropertySpecSyntax
    semi: Token
    variables: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PropertyExprSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PropertySpecSyntax(SyntaxNode):
    clocking: TimingControlSyntax
    disable: DisableIffSyntax
    expr: PropertyExprSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PropertySymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def ports(self) -> span[AssertionPortSymbol]:
        ...
class PropertyType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PullStrengthSyntax(NetStrengthSyntax):
    closeParen: Token
    openParen: Token
    strength: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PulseStyleDeclarationSyntax(MemberSyntax):
    inputs: ...
    keyword: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class PulseStyleKind:
    """
    Members:

      OnEvent

      OnDetect

      ShowCancelled

      NoShowCancelled
    """
    NoShowCancelled: typing.ClassVar[PulseStyleKind]  # value = <PulseStyleKind.NoShowCancelled: 3>
    OnDetect: typing.ClassVar[PulseStyleKind]  # value = <PulseStyleKind.OnDetect: 1>
    OnEvent: typing.ClassVar[PulseStyleKind]  # value = <PulseStyleKind.OnEvent: 0>
    ShowCancelled: typing.ClassVar[PulseStyleKind]  # value = <PulseStyleKind.ShowCancelled: 2>
    __members__: typing.ClassVar[dict[str, PulseStyleKind]]  # value = {'OnEvent': <PulseStyleKind.OnEvent: 0>, 'OnDetect': <PulseStyleKind.OnDetect: 1>, 'ShowCancelled': <PulseStyleKind.ShowCancelled: 2>, 'NoShowCancelled': <PulseStyleKind.NoShowCancelled: 3>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PulseStyleSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def pulseStyleKind(self) -> PulseStyleKind:
        ...
    @property
    def terminals(self) -> span[Expression]:
        ...
class QueueDimensionSpecifierSyntax(DimensionSpecifierSyntax):
    dollar: Token
    maxSizeClause: ColonExpressionClauseSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class QueueType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def elementType(self) -> Type:
        ...
    @property
    def maxBound(self) -> int:
        ...
class RandCaseItemSyntax(SyntaxNode):
    colon: Token
    expr: ExpressionSyntax
    statement: StatementSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RandCaseStatement(Statement):
    class Item:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def stmt(self) -> Statement:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def items(self) -> span[...]:
        ...
class RandCaseStatementSyntax(StatementSyntax):
    endCase: Token
    items: ...
    randCase: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RandJoinClauseSyntax(SyntaxNode):
    expr: ParenthesizedExpressionSyntax
    join: Token
    rand: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RandMode:
    """
    Members:

      None

      Rand

      RandC
    """
    None: typing.ClassVar[RandMode]  # value = <RandMode.None: 0>
    Rand: typing.ClassVar[RandMode]  # value = <RandMode.Rand: 1>
    RandC: typing.ClassVar[RandMode]  # value = <RandMode.RandC: 2>
    __members__: typing.ClassVar[dict[str, RandMode]]  # value = {'None': <RandMode.None: 0>, 'Rand': <RandMode.Rand: 1>, 'RandC': <RandMode.RandC: 2>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class RandSeqProductionSymbol(Symbol, Scope):
    class CaseItem:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def expressions(self) -> span[Expression]:
            ...
        @property
        def item(self) -> RandSeqProductionSymbol.ProdItem:
            ...
    class CaseProd(RandSeqProductionSymbol.ProdBase):
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def defaultItem(self) -> RandSeqProductionSymbol.ProdItem | None:
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def items(self) -> span[RandSeqProductionSymbol.CaseItem]:
            ...
    class CodeBlockProd(RandSeqProductionSymbol.ProdBase):
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def block(self) -> StatementBlockSymbol:
            ...
    class IfElseProd(RandSeqProductionSymbol.ProdBase):
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def elseItem(self) -> RandSeqProductionSymbol.ProdItem | None:
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def ifItem(self) -> RandSeqProductionSymbol.ProdItem:
            ...
    class ProdBase:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def kind(self) -> RandSeqProductionSymbol.ProdKind:
            ...
    class ProdItem(RandSeqProductionSymbol.ProdBase):
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def args(self) -> span[Expression]:
            ...
        @property
        def target(self) -> RandSeqProductionSymbol:
            ...
    class ProdKind:
        """
        Members:

          Item

          CodeBlock

          IfElse

          Repeat

          Case
        """
        Case: typing.ClassVar[RandSeqProductionSymbol.ProdKind]  # value = <ProdKind.Case: 4>
        CodeBlock: typing.ClassVar[RandSeqProductionSymbol.ProdKind]  # value = <ProdKind.CodeBlock: 1>
        IfElse: typing.ClassVar[RandSeqProductionSymbol.ProdKind]  # value = <ProdKind.IfElse: 2>
        Item: typing.ClassVar[RandSeqProductionSymbol.ProdKind]  # value = <ProdKind.Item: 0>
        Repeat: typing.ClassVar[RandSeqProductionSymbol.ProdKind]  # value = <ProdKind.Repeat: 3>
        __members__: typing.ClassVar[dict[str, RandSeqProductionSymbol.ProdKind]]  # value = {'Item': <ProdKind.Item: 0>, 'CodeBlock': <ProdKind.CodeBlock: 1>, 'IfElse': <ProdKind.IfElse: 2>, 'Repeat': <ProdKind.Repeat: 3>, 'Case': <ProdKind.Case: 4>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class RepeatProd(RandSeqProductionSymbol.ProdBase):
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def item(self) -> RandSeqProductionSymbol.ProdItem:
            ...
    class Rule:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def codeBlock(self) -> RandSeqProductionSymbol.CodeBlockProd | None:
            ...
        @property
        def isRandJoin(self) -> bool:
            ...
        @property
        def prods(self) -> span[RandSeqProductionSymbol.ProdBase]:
            ...
        @property
        def randJoinExpr(self) -> Expression:
            ...
        @property
        def ruleBlock(self) -> StatementBlockSymbol:
            ...
        @property
        def weightExpr(self) -> Expression:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arguments(self) -> span[FormalArgumentSymbol]:
        ...
    @property
    def returnType(self) -> ...:
        ...
    @property
    def rules(self) -> span[...]:
        ...
class RandSequenceStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def firstProduction(self) -> ...:
        ...
class RandSequenceStatementSyntax(StatementSyntax):
    closeParen: Token
    endsequence: Token
    firstProduction: Token
    openParen: Token
    productions: ...
    randsequence: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RangeCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    ranges: RangeListSyntax
    withClause: WithClauseSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RangeDimensionSpecifierSyntax(DimensionSpecifierSyntax):
    selector: SelectorSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RangeListSyntax(SyntaxNode):
    closeBrace: Token
    openBrace: Token
    valueRanges: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RangeSelectExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def left(self) -> Expression:
        ...
    @property
    def right(self) -> Expression:
        ...
    @property
    def selectionKind(self) -> RangeSelectionKind:
        ...
    @property
    def value(self) -> Expression:
        ...
class RangeSelectSyntax(SelectorSyntax):
    left: ExpressionSyntax
    range: Token
    right: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RangeSelectionKind:
    """
    Members:

      Simple

      IndexedUp

      IndexedDown
    """
    IndexedDown: typing.ClassVar[RangeSelectionKind]  # value = <RangeSelectionKind.IndexedDown: 2>
    IndexedUp: typing.ClassVar[RangeSelectionKind]  # value = <RangeSelectionKind.IndexedUp: 1>
    Simple: typing.ClassVar[RangeSelectionKind]  # value = <RangeSelectionKind.Simple: 0>
    __members__: typing.ClassVar[dict[str, RangeSelectionKind]]  # value = {'Simple': <RangeSelectionKind.Simple: 0>, 'IndexedUp': <RangeSelectionKind.IndexedUp: 1>, 'IndexedDown': <RangeSelectionKind.IndexedDown: 2>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class RealLiteral(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def value(self) -> float:
        ...
class RepeatLoopStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def body(self) -> Statement:
        ...
    @property
    def count(self) -> Expression:
        ...
class RepeatedEventControl(TimingControl):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def event(self) -> TimingControl:
        ...
    @property
    def expr(self) -> ...:
        ...
class RepeatedEventControlSyntax(TimingControlSyntax):
    closeParen: Token
    eventControl: TimingControlSyntax
    expr: ExpressionSyntax
    openParen: Token
    repeat: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ReplicatedAssignmentPatternExpression(AssignmentPatternExpressionBase):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def count(self) -> Expression:
        ...
class ReplicatedAssignmentPatternSyntax(AssignmentPatternSyntax):
    closeBrace: Token
    countExpr: ExpressionSyntax
    innerCloseBrace: Token
    innerOpenBrace: Token
    items: ...
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ReplicationExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def concat(self) -> Expression:
        ...
    @property
    def count(self) -> Expression:
        ...
class ReportedDiagnostic:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expansionLocs(self) -> span[SourceLocation]:
        ...
    @property
    def formattedMessage(self) -> str:
        ...
    @property
    def location(self) -> SourceLocation:
        ...
    @property
    def originalDiagnostic(self) -> Diagnostic:
        ...
    @property
    def ranges(self) -> span[SourceRange]:
        ...
    @property
    def severity(self) -> DiagnosticSeverity:
        ...
    @property
    def shouldShowIncludeStack(self) -> bool:
        ...
class ReturnStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> Expression:
        ...
class ReturnStatementSyntax(StatementSyntax):
    returnKeyword: Token
    returnValue: ExpressionSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RootSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def compilationUnits(self) -> span[CompilationUnitSymbol]:
        ...
    @property
    def topInstances(self) -> span[...]:
        ...
class RsCaseItemSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RsCaseSyntax(RsProdSyntax):
    closeParen: Token
    endcase: Token
    expr: ExpressionSyntax
    items: ...
    keyword: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RsCodeBlockSyntax(RsProdSyntax):
    closeBrace: Token
    items: ...
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RsElseClauseSyntax(SyntaxNode):
    item: RsProdItemSyntax
    keyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RsIfElseSyntax(RsProdSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    elseClause: RsElseClauseSyntax
    ifItem: RsProdItemSyntax
    keyword: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RsProdItemSyntax(RsProdSyntax):
    argList: ArgumentListSyntax
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RsProdSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RsRepeatSyntax(RsProdSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    item: RsProdItemSyntax
    keyword: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RsRuleSyntax(SyntaxNode):
    prods: ...
    randJoin: RandJoinClauseSyntax
    weightClause: RsWeightClauseSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class RsWeightClauseSyntax(SyntaxNode):
    codeBlock: RsProdSyntax
    colonEqual: Token
    weight: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SVInt:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def concat(arg0: span[SVInt]) -> SVInt:
        ...
    @staticmethod
    def conditional(condition: SVInt, lhs: SVInt, rhs: SVInt) -> SVInt:
        ...
    @staticmethod
    def createFillX(bitWidth: int, isSigned: bool) -> SVInt:
        ...
    @staticmethod
    def createFillZ(bitWidth: int, isSigned: bool) -> SVInt:
        ...
    @staticmethod
    def fromDigits(bits: int, base: LiteralBase, isSigned: bool, anyUnknown: bool, digits: span[logic_t]) -> SVInt:
        ...
    @staticmethod
    def fromDouble(bits: int, value: float, isSigned: bool, round: bool = True) -> SVInt:
        ...
    @staticmethod
    def fromFloat(bits: int, value: float, isSigned: bool, round: bool = True) -> SVInt:
        ...
    @staticmethod
    def logicalEquiv(lhs: SVInt, rhs: SVInt) -> logic_t:
        ...
    @staticmethod
    def logicalImpl(lhs: SVInt, rhs: SVInt) -> logic_t:
        ...
    @typing.overload
    def __add__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __add__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __and__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __and__(self, arg0: int) -> SVInt:
        ...
    def __bool__(self) -> bool:
        ...
    @typing.overload
    def __eq__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __eq__(self, arg0: int) -> logic_t:
        ...
    def __float__(self) -> float:
        ...
    @typing.overload
    def __ge__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __ge__(self, arg0: int) -> logic_t:
        ...
    def __getitem__(self, arg0: int) -> logic_t:
        ...
    @typing.overload
    def __gt__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __gt__(self, arg0: int) -> logic_t:
        ...
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __iadd__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __iadd__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __iand__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __iand__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __imod__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __imod__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __imul__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __imul__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, bit: logic_t) -> None:
        ...
    @typing.overload
    def __init__(self, bits: int, value: int, isSigned: bool) -> None:
        ...
    @typing.overload
    def __init__(self, bits: int, bytes: span[...], isSigned: bool) -> None:
        ...
    @typing.overload
    def __init__(self, str: str) -> None:
        ...
    @typing.overload
    def __init__(self, value: float) -> None:
        ...
    @typing.overload
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> SVInt:
        ...
    @typing.overload
    def __ior__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __ior__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __isub__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __isub__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __itruediv__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __itruediv__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __ixor__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __ixor__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __le__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __le__(self, arg0: int) -> logic_t:
        ...
    @typing.overload
    def __lt__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __lt__(self, arg0: int) -> logic_t:
        ...
    @typing.overload
    def __mod__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __mod__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __mul__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __mul__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __ne__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __ne__(self, arg0: int) -> logic_t:
        ...
    def __neg__(self) -> SVInt:
        ...
    @typing.overload
    def __or__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __or__(self, arg0: int) -> SVInt:
        ...
    def __pow__(self, arg0: SVInt) -> SVInt:
        ...
    def __radd__(self, arg0: int) -> SVInt:
        ...
    def __rand__(self, arg0: int) -> SVInt:
        ...
    def __rdiv__(self, arg0: int) -> SVInt:
        ...
    def __repr__(self) -> str:
        ...
    def __rmod__(self, arg0: int) -> SVInt:
        ...
    def __rmul__(self, arg0: int) -> SVInt:
        ...
    def __ror__(self, arg0: int) -> SVInt:
        ...
    def __rsub__(self, arg0: int) -> SVInt:
        ...
    def __rxor__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __sub__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __sub__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __truediv__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __truediv__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __xor__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __xor__(self, arg0: int) -> SVInt:
        ...
    def ashr(self, rhs: SVInt) -> SVInt:
        ...
    def countLeadingOnes(self) -> int:
        ...
    def countLeadingUnknowns(self) -> int:
        ...
    def countLeadingZeros(self) -> int:
        ...
    def countLeadingZs(self) -> int:
        ...
    def countOnes(self) -> int:
        ...
    def countXs(self) -> int:
        ...
    def countZeros(self) -> int:
        ...
    def countZs(self) -> int:
        ...
    def extend(self, bits: int, isSigned: bool) -> SVInt:
        ...
    def flattenUnknowns(self) -> None:
        ...
    def getActiveBits(self) -> int:
        ...
    def getMinRepresentedBits(self) -> int:
        ...
    def isEven(self) -> bool:
        ...
    def isNegative(self) -> bool:
        ...
    def isOdd(self) -> bool:
        ...
    def isSignExtendedFrom(self, msb: int) -> bool:
        ...
    def lshr(self, rhs: SVInt) -> SVInt:
        ...
    def reductionAnd(self) -> logic_t:
        ...
    def reductionOr(self) -> logic_t:
        ...
    def reductionXor(self) -> logic_t:
        ...
    def replicate(self, times: SVInt) -> SVInt:
        ...
    def resize(self, bits: int) -> SVInt:
        ...
    def reverse(self) -> SVInt:
        ...
    def set(self, msb: int, lsb: int, value: SVInt) -> None:
        ...
    def setAllOnes(self) -> None:
        ...
    def setAllX(self) -> None:
        ...
    def setAllZ(self) -> None:
        ...
    def setAllZeros(self) -> None:
        ...
    def setSigned(self, isSigned: bool) -> None:
        ...
    def sext(self, bits: int) -> SVInt:
        ...
    def shl(self, rhs: SVInt) -> SVInt:
        ...
    def shrinkToFit(self) -> None:
        ...
    def signExtendFrom(self, msb: int) -> None:
        ...
    def slice(self, msb: int, lsb: int) -> SVInt:
        ...
    def toString(self, base: LiteralBase, includeBase: bool, abbreviateThresholdBits: int = 16777215) -> str:
        ...
    def trunc(self, bits: int) -> SVInt:
        ...
    def xnor(self, rhs: SVInt) -> SVInt:
        ...
    def zext(self, bits: int) -> SVInt:
        ...
    @property
    def bitWidth(self) -> int:
        ...
    @property
    def hasUnknown(self) -> bool:
        ...
    @property
    def isSigned(self) -> bool:
        ...
class ScalarType(IntegralType):
    class Kind:
        """
        Members:

          Bit

          Logic

          Reg
        """
        Bit: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Bit: 0>
        Logic: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Logic: 1>
        Reg: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Reg: 2>
        __members__: typing.ClassVar[dict[str, ScalarType.Kind]]  # value = {'Bit': <Kind.Bit: 0>, 'Logic': <Kind.Logic: 1>, 'Reg': <Kind.Reg: 2>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Bit: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Bit: 0>
    Logic: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Logic: 1>
    Reg: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Reg: 2>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def scalarKind(self) -> ...:
        ...
class Scope:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __getitem__(self, arg0: int) -> typing.Any:
        ...
    def __iter__(self) -> typing.Iterator[Symbol]:
        ...
    def __len__(self) -> int:
        ...
    def find(self, arg0: str) -> Symbol:
        ...
    def lookupName(self, name: str, location: LookupLocation = ..., flags: LookupFlags = ...) -> Symbol:
        ...
    @property
    def compilation(self) -> Compilation:
        ...
    @property
    def compilationUnit(self) -> ...:
        ...
    @property
    def containingInstance(self) -> ...:
        ...
    @property
    def defaultNetType(self) -> ...:
        ...
    @property
    def isProceduralContext(self) -> bool:
        ...
    @property
    def isUninstantiated(self) -> bool:
        ...
    @property
    def timeScale(self) -> TimeScale | None:
        ...
class ScopedNameSyntax(NameSyntax):
    left: NameSyntax
    right: NameSyntax
    separator: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ScriptSession:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def eval(self, text: str) -> ...:
        ...
    def evalExpression(self, expr: ...) -> ...:
        ...
    def evalStatement(self, expr: ...) -> None:
        ...
    def getDiagnostics(self) -> ...:
        ...
    @property
    def compilation(self) -> Compilation:
        ...
class SelectorSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SequenceConcatExpr(AssertionExpr):
    class Element:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def delay(self) -> SequenceRange:
            ...
        @property
        def sequence(self) -> AssertionExpr:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def elements(self) -> span[...]:
        ...
class SequenceDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    keyword: Token
    name: Token
    optionalSemi: Token
    portList: AssertionItemPortListSyntax
    semi: Token
    seqExpr: SequenceExprSyntax
    variables: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SequenceExprSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SequenceMatchListSyntax(SyntaxNode):
    comma: Token
    items: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SequenceRange:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def max(self) -> int | None:
        ...
    @property
    def min(self) -> int:
        ...
class SequenceRepetition:
    class Kind:
        """
        Members:

          Consecutive

          Nonconsecutive

          GoTo
        """
        Consecutive: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.Consecutive: 0>
        GoTo: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.GoTo: 2>
        Nonconsecutive: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.Nonconsecutive: 1>
        __members__: typing.ClassVar[dict[str, SequenceRepetition.Kind]]  # value = {'Consecutive': <Kind.Consecutive: 0>, 'Nonconsecutive': <Kind.Nonconsecutive: 1>, 'GoTo': <Kind.GoTo: 2>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Consecutive: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.Consecutive: 0>
    GoTo: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.GoTo: 2>
    Nonconsecutive: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.Nonconsecutive: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def kind(self) -> ...:
        ...
    @property
    def range(self) -> SequenceRange:
        ...
class SequenceRepetitionSyntax(SyntaxNode):
    closeBracket: Token
    op: Token
    openBracket: Token
    selector: SelectorSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SequenceSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def ports(self) -> span[AssertionPortSymbol]:
        ...
class SequenceType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SequenceWithMatchExpr(AssertionExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> AssertionExpr:
        ...
    @property
    def matchItems(self) -> span[...]:
        ...
    @property
    def repetition(self) -> SequenceRepetition | None:
        ...
class SetExprBinsSelectExpr(BinsSelectExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> ...:
        ...
    @property
    def matchesExpr(self) -> ...:
        ...
class SignalEventControl(TimingControl):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def edge(self) -> ...:
        ...
    @property
    def expr(self) -> ...:
        ...
    @property
    def iffCondition(self) -> ...:
        ...
class SignalEventExpressionSyntax(EventExpressionSyntax):
    edge: Token
    expr: ExpressionSyntax
    iffClause: IffEventClauseSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SignedCastExpressionSyntax(ExpressionSyntax):
    apostrophe: Token
    inner: ParenthesizedExpressionSyntax
    signing: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SimpleAssertionExpr(AssertionExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> ...:
        ...
    @property
    def repetition(self) -> SequenceRepetition | None:
        ...
class SimpleAssignmentPatternExpression(AssignmentPatternExpressionBase):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SimpleAssignmentPatternSyntax(AssignmentPatternSyntax):
    closeBrace: Token
    items: ...
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SimpleBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    expr: ExpressionSyntax
    matchesClause: MatchesClauseSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SimpleDirectiveSyntax(DirectiveSyntax):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SimplePathSuffixSyntax(PathSuffixSyntax):
    outputs: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SimplePragmaExpressionSyntax(PragmaExpressionSyntax):
    value: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SimplePropertyExprSyntax(PropertyExprSyntax):
    expr: SequenceExprSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SimpleSequenceExprSyntax(SequenceExprSyntax):
    expr: ExpressionSyntax
    repetition: SequenceRepetitionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SimpleSystemSubroutine(SystemSubroutine):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, name: str, kind: SubroutineKind, requiredArgs: int, argTypes: list[...], returnType: ..., isMethod: bool, isFirstArgLValue: bool = False) -> None:
        ...
class SolveBeforeConstraint(Constraint):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def after(self) -> span[...]:
        ...
    @property
    def solve(self) -> span[...]:
        ...
class SolveBeforeConstraintSyntax(ConstraintItemSyntax):
    afterExpr: ...
    before: Token
    beforeExpr: ...
    semi: Token
    solve: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SourceBuffer:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __bool__(self) -> bool:
        ...
    def __init__(self) -> None:
        ...
    @property
    def data(self) -> str:
        ...
    @property
    def id(self) -> BufferID:
        ...
    @property
    def library(self) -> SourceLibrary:
        ...
class SourceLibrary:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    @property
    def name(self) -> str:
        ...
class SourceLoader:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, sourceManager: ...) -> None:
        ...
    def addFiles(self, pattern: str) -> None:
        ...
    def addLibraryFiles(self, libraryName: str, pattern: str) -> None:
        ...
    def addLibraryMaps(self, pattern: str, basePath: os.PathLike, optionBag: ...) -> None:
        ...
    def addSearchDirectories(self, pattern: str) -> None:
        ...
    def addSearchExtension(self, extension: str) -> None:
        ...
    def addSeparateUnit(self, filePatterns: span[str], includePaths: list[str], defines: list[str], libraryName: str) -> None:
        ...
    def loadAndParseSources(self, optionBag: ...) -> list[...]:
        ...
    def loadSources(self) -> list[...]:
        ...
    @property
    def errors(self) -> span[str]:
        ...
    @property
    def hasFiles(self) -> bool:
        ...
    @property
    def libraryMaps(self) -> list[...]:
        ...
class SourceLocation:
    NoLocation: typing.ClassVar[SourceLocation]  # value = SourceLocation(268435455, 68719476735)
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: SourceLocation) -> bool:
        ...
    def __ge__(self, arg0: SourceLocation) -> bool:
        ...
    def __gt__(self, arg0: SourceLocation) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, buffer: BufferID, offset: int) -> None:
        ...
    def __le__(self, arg0: SourceLocation) -> bool:
        ...
    def __lt__(self, arg0: SourceLocation) -> bool:
        ...
    def __ne__(self, arg0: SourceLocation) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def buffer(self) -> BufferID:
        ...
    @property
    def offset(self) -> int:
        ...
class SourceManager:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def addDiagnosticDirective(self, location: SourceLocation, name: str, severity: ...) -> None:
        ...
    def addLineDirective(self, location: SourceLocation, lineNum: int, name: str, level: int) -> None:
        ...
    def addSystemDirectories(self, path: str) -> None:
        ...
    def addUserDirectories(self, path: str) -> None:
        ...
    @typing.overload
    def assignText(self, text: str, includedFrom: SourceLocation = ..., library: SourceLibrary = None) -> SourceBuffer:
        ...
    @typing.overload
    def assignText(self, path: str, text: str, includedFrom: SourceLocation = ..., library: SourceLibrary = None) -> SourceBuffer:
        ...
    def getAllBuffers(self) -> list[BufferID]:
        ...
    def getColumnNumber(self, location: SourceLocation) -> int:
        ...
    def getExpansionLoc(self, location: SourceLocation) -> SourceLocation:
        ...
    def getExpansionRange(self, location: SourceLocation) -> SourceRange:
        ...
    def getFileName(self, location: SourceLocation) -> str:
        ...
    def getFullPath(self, buffer: BufferID) -> os.PathLike:
        ...
    def getFullyExpandedLoc(self, location: SourceLocation) -> SourceLocation:
        ...
    def getFullyOriginalLoc(self, location: SourceLocation) -> SourceLocation:
        ...
    def getFullyOriginalRange(self, range: SourceRange) -> SourceRange:
        ...
    def getIncludedFrom(self, buffer: BufferID) -> SourceLocation:
        ...
    def getLineNumber(self, location: SourceLocation) -> int:
        ...
    def getMacroName(self, location: SourceLocation) -> str:
        ...
    def getOriginalLoc(self, location: SourceLocation) -> SourceLocation:
        ...
    def getRawFileName(self, buffer: BufferID) -> str:
        ...
    def getSourceText(self, buffer: BufferID) -> str:
        ...
    def isBeforeInCompilationUnit(self, left: SourceLocation, right: SourceLocation) -> bool | None:
        ...
    def isCached(self, path: os.PathLike) -> bool:
        ...
    def isFileLoc(self, location: SourceLocation) -> bool:
        ...
    def isIncludedFileLoc(self, location: SourceLocation) -> bool:
        ...
    def isMacroArgLoc(self, location: SourceLocation) -> bool:
        ...
    def isMacroLoc(self, location: SourceLocation) -> bool:
        ...
    def isPreprocessedLoc(self, location: SourceLocation) -> bool:
        ...
    def readHeader(self, path: str, includedFrom: SourceLocation, library: SourceLibrary, isSystemPath: bool) -> SourceBuffer:
        ...
    def readSource(self, path: os.PathLike, library: SourceLibrary = None) -> SourceBuffer:
        ...
    def setDisableProximatePaths(self, set: bool) -> None:
        ...
class SourceOptions:
    librariesInheritMacros: bool
    numThreads: int | None
    onlyLint: bool
    singleUnit: bool
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
class SourceRange:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, arg0: SourceRange) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, startLoc: SourceLocation, endLoc: SourceLocation) -> None:
        ...
    def __ne__(self, arg0: SourceRange) -> bool:
        ...
    @property
    def end(self) -> SourceLocation:
        ...
    @property
    def start(self) -> SourceLocation:
        ...
class SpecifyBlockSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SpecifyBlockSyntax(MemberSyntax):
    endspecify: Token
    items: ...
    specify: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SpecparamDeclarationSyntax(MemberSyntax):
    declarators: ...
    keyword: Token
    semi: Token
    type: ImplicitTypeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SpecparamDeclaratorSyntax(SyntaxNode):
    closeParen: Token
    comma: Token
    equals: Token
    name: Token
    openParen: Token
    value1: ExpressionSyntax
    value2: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SpecparamSymbol(ValueSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def isPathPulse(self) -> bool:
        ...
    @property
    def pathDest(self) -> Symbol:
        ...
    @property
    def pathSource(self) -> Symbol:
        ...
    @property
    def pulseErrorLimit(self) -> ConstantValue:
        ...
    @property
    def pulseRejectLimit(self) -> ConstantValue:
        ...
    @property
    def value(self) -> ConstantValue:
        ...
class StandardCaseItemSyntax(CaseItemSyntax):
    clause: SyntaxNode
    colon: Token
    expressions: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StandardPropertyCaseItemSyntax(PropertyCaseItemSyntax):
    colon: Token
    expr: PropertyExprSyntax
    expressions: ...
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StandardRsCaseItemSyntax(RsCaseItemSyntax):
    colon: Token
    expressions: ...
    item: RsProdItemSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class Statement:
    class EvalResult:
        """
        Members:

          Fail

          Success

          Return

          Break

          Continue

          Disable
        """
        Break: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Break: 3>
        Continue: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Continue: 4>
        Disable: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Disable: 5>
        Fail: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Fail: 0>
        Return: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Return: 2>
        Success: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Success: 1>
        __members__: typing.ClassVar[dict[str, Statement.EvalResult]]  # value = {'Fail': <EvalResult.Fail: 0>, 'Success': <EvalResult.Success: 1>, 'Return': <EvalResult.Return: 2>, 'Break': <EvalResult.Break: 3>, 'Continue': <EvalResult.Continue: 4>, 'Disable': <EvalResult.Disable: 5>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __repr__(self) -> str:
        ...
    def eval(self, context: EvalContext) -> ...:
        ...
    def visit(self, f: typing.Any) -> None:
        """
        Visit a pyslang object with a callback f.

        If f ever returns pyslang.VisitAction.Interrupt, the visit is aborted, and no additional nodes are visited. If f returns pyslang.VisitAction.Skip, then no child nodes of the current node are visited, but otherwise the visit continues. Any other return value, including pslang.VisitAction.Advance is ignored, and the walk continues.
        """
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> StatementKind:
        ...
    @property
    def sourceRange(self) -> SourceRange:
        ...
    @property
    def syntax(self) -> ...:
        ...
class StatementBlockKind:
    """
    Members:

      Sequential

      JoinAll

      JoinAny

      JoinNone
    """
    JoinAll: typing.ClassVar[StatementBlockKind]  # value = <StatementBlockKind.JoinAll: 1>
    JoinAny: typing.ClassVar[StatementBlockKind]  # value = <StatementBlockKind.JoinAny: 2>
    JoinNone: typing.ClassVar[StatementBlockKind]  # value = <StatementBlockKind.JoinNone: 3>
    Sequential: typing.ClassVar[StatementBlockKind]  # value = <StatementBlockKind.Sequential: 0>
    __members__: typing.ClassVar[dict[str, StatementBlockKind]]  # value = {'Sequential': <StatementBlockKind.Sequential: 0>, 'JoinAll': <StatementBlockKind.JoinAll: 1>, 'JoinAny': <StatementBlockKind.JoinAny: 2>, 'JoinNone': <StatementBlockKind.JoinNone: 3>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StatementBlockSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def blockKind(self) -> StatementBlockKind:
        ...
    @property
    def defaultLifetime(self) -> VariableLifetime:
        ...
class StatementKind:
    """
    Members:

      Invalid

      Empty

      List

      Block

      ExpressionStatement

      VariableDeclaration

      Return

      Continue

      Break

      Disable

      Conditional

      Case

      PatternCase

      ForLoop

      RepeatLoop

      ForeachLoop

      WhileLoop

      DoWhileLoop

      ForeverLoop

      Timed

      ImmediateAssertion

      ConcurrentAssertion

      DisableFork

      Wait

      WaitFork

      WaitOrder

      EventTrigger

      ProceduralAssign

      ProceduralDeassign

      RandCase

      RandSequence

      ProceduralChecker
    """
    Block: typing.ClassVar[StatementKind]  # value = <StatementKind.Block: 3>
    Break: typing.ClassVar[StatementKind]  # value = <StatementKind.Break: 8>
    Case: typing.ClassVar[StatementKind]  # value = <StatementKind.Case: 11>
    ConcurrentAssertion: typing.ClassVar[StatementKind]  # value = <StatementKind.ConcurrentAssertion: 21>
    Conditional: typing.ClassVar[StatementKind]  # value = <StatementKind.Conditional: 10>
    Continue: typing.ClassVar[StatementKind]  # value = <StatementKind.Continue: 7>
    Disable: typing.ClassVar[StatementKind]  # value = <StatementKind.Disable: 9>
    DisableFork: typing.ClassVar[StatementKind]  # value = <StatementKind.DisableFork: 22>
    DoWhileLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.DoWhileLoop: 17>
    Empty: typing.ClassVar[StatementKind]  # value = <StatementKind.Empty: 1>
    EventTrigger: typing.ClassVar[StatementKind]  # value = <StatementKind.EventTrigger: 26>
    ExpressionStatement: typing.ClassVar[StatementKind]  # value = <StatementKind.ExpressionStatement: 4>
    ForLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.ForLoop: 13>
    ForeachLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.ForeachLoop: 15>
    ForeverLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.ForeverLoop: 18>
    ImmediateAssertion: typing.ClassVar[StatementKind]  # value = <StatementKind.ImmediateAssertion: 20>
    Invalid: typing.ClassVar[StatementKind]  # value = <StatementKind.Invalid: 0>
    List: typing.ClassVar[StatementKind]  # value = <StatementKind.List: 2>
    PatternCase: typing.ClassVar[StatementKind]  # value = <StatementKind.PatternCase: 12>
    ProceduralAssign: typing.ClassVar[StatementKind]  # value = <StatementKind.ProceduralAssign: 27>
    ProceduralChecker: typing.ClassVar[StatementKind]  # value = <StatementKind.ProceduralChecker: 31>
    ProceduralDeassign: typing.ClassVar[StatementKind]  # value = <StatementKind.ProceduralDeassign: 28>
    RandCase: typing.ClassVar[StatementKind]  # value = <StatementKind.RandCase: 29>
    RandSequence: typing.ClassVar[StatementKind]  # value = <StatementKind.RandSequence: 30>
    RepeatLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.RepeatLoop: 14>
    Return: typing.ClassVar[StatementKind]  # value = <StatementKind.Return: 6>
    Timed: typing.ClassVar[StatementKind]  # value = <StatementKind.Timed: 19>
    VariableDeclaration: typing.ClassVar[StatementKind]  # value = <StatementKind.VariableDeclaration: 5>
    Wait: typing.ClassVar[StatementKind]  # value = <StatementKind.Wait: 23>
    WaitFork: typing.ClassVar[StatementKind]  # value = <StatementKind.WaitFork: 24>
    WaitOrder: typing.ClassVar[StatementKind]  # value = <StatementKind.WaitOrder: 25>
    WhileLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.WhileLoop: 16>
    __members__: typing.ClassVar[dict[str, StatementKind]]  # value = {'Invalid': <StatementKind.Invalid: 0>, 'Empty': <StatementKind.Empty: 1>, 'List': <StatementKind.List: 2>, 'Block': <StatementKind.Block: 3>, 'ExpressionStatement': <StatementKind.ExpressionStatement: 4>, 'VariableDeclaration': <StatementKind.VariableDeclaration: 5>, 'Return': <StatementKind.Return: 6>, 'Continue': <StatementKind.Continue: 7>, 'Break': <StatementKind.Break: 8>, 'Disable': <StatementKind.Disable: 9>, 'Conditional': <StatementKind.Conditional: 10>, 'Case': <StatementKind.Case: 11>, 'PatternCase': <StatementKind.PatternCase: 12>, 'ForLoop': <StatementKind.ForLoop: 13>, 'RepeatLoop': <StatementKind.RepeatLoop: 14>, 'ForeachLoop': <StatementKind.ForeachLoop: 15>, 'WhileLoop': <StatementKind.WhileLoop: 16>, 'DoWhileLoop': <StatementKind.DoWhileLoop: 17>, 'ForeverLoop': <StatementKind.ForeverLoop: 18>, 'Timed': <StatementKind.Timed: 19>, 'ImmediateAssertion': <StatementKind.ImmediateAssertion: 20>, 'ConcurrentAssertion': <StatementKind.ConcurrentAssertion: 21>, 'DisableFork': <StatementKind.DisableFork: 22>, 'Wait': <StatementKind.Wait: 23>, 'WaitFork': <StatementKind.WaitFork: 24>, 'WaitOrder': <StatementKind.WaitOrder: 25>, 'EventTrigger': <StatementKind.EventTrigger: 26>, 'ProceduralAssign': <StatementKind.ProceduralAssign: 27>, 'ProceduralDeassign': <StatementKind.ProceduralDeassign: 28>, 'RandCase': <StatementKind.RandCase: 29>, 'RandSequence': <StatementKind.RandSequence: 30>, 'ProceduralChecker': <StatementKind.ProceduralChecker: 31>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StatementList(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def list(self) -> span[Statement]:
        ...
class StatementSyntax(SyntaxNode):
    attributes: ...
    label: NamedLabelSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StreamExpressionSyntax(SyntaxNode):
    expression: ExpressionSyntax
    withRange: StreamExpressionWithRangeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StreamExpressionWithRangeSyntax(SyntaxNode):
    range: ElementSelectSyntax
    withKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StreamingConcatenationExpression(Expression):
    class StreamExpression:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def constantWithWidth(self) -> int | None:
            ...
        @property
        def operand(self) -> Expression:
            ...
        @property
        def withExpr(self) -> Expression:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def bitstreamWidth(self) -> int:
        ...
    @property
    def isFixedSize(self) -> bool:
        ...
    @property
    def sliceSize(self) -> int:
        ...
    @property
    def streams(self) -> span[...]:
        ...
class StreamingConcatenationExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    expressions: ...
    innerCloseBrace: Token
    innerOpenBrace: Token
    openBrace: Token
    operatorToken: Token
    sliceSize: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StringLiteral(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def intValue(self) -> ...:
        ...
    @property
    def rawValue(self) -> str:
        ...
    @property
    def value(self) -> str:
        ...
class StringType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StrongWeakAssertionExpr(AssertionExpr):
    class Strength:
        """
        Members:

          Strong

          Weak
        """
        Strong: typing.ClassVar[StrongWeakAssertionExpr.Strength]  # value = <Strength.Strong: 0>
        Weak: typing.ClassVar[StrongWeakAssertionExpr.Strength]  # value = <Strength.Weak: 1>
        __members__: typing.ClassVar[dict[str, StrongWeakAssertionExpr.Strength]]  # value = {'Strong': <Strength.Strong: 0>, 'Weak': <Strength.Weak: 1>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Strong: typing.ClassVar[StrongWeakAssertionExpr.Strength]  # value = <Strength.Strong: 0>
    Weak: typing.ClassVar[StrongWeakAssertionExpr.Strength]  # value = <Strength.Weak: 1>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> AssertionExpr:
        ...
    @property
    def strength(self) -> ...:
        ...
class StrongWeakPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    expr: SequenceExprSyntax
    keyword: Token
    openParen: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StructUnionMemberSyntax(SyntaxNode):
    attributes: ...
    declarators: ...
    randomQualifier: Token
    semi: Token
    type: DataTypeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StructUnionTypeSyntax(DataTypeSyntax):
    closeBrace: Token
    dimensions: ...
    keyword: Token
    members: ...
    openBrace: Token
    packed: Token
    signing: Token
    taggedOrSoft: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StructurePattern(Pattern):
    class FieldPattern:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def field(self) -> ...:
            ...
        @property
        def pattern(self) -> Pattern:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def patterns(self) -> span[...]:
        ...
class StructurePatternMemberSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StructurePatternSyntax(PatternSyntax):
    closeBrace: Token
    members: ...
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class StructuredAssignmentPatternExpression(AssignmentPatternExpressionBase):
    class IndexSetter:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def index(self) -> Expression:
            ...
    class MemberSetter:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def member(self) -> ...:
            ...
    class TypeSetter:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def type(self) -> ...:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def defaultSetter(self) -> Expression:
        ...
    @property
    def indexSetters(self) -> span[...]:
        ...
    @property
    def memberSetters(self) -> span[...]:
        ...
    @property
    def typeSetters(self) -> span[...]:
        ...
class StructuredAssignmentPatternSyntax(AssignmentPatternSyntax):
    closeBrace: Token
    items: ...
    openBrace: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SubroutineKind:
    """
    Members:

      Function

      Task
    """
    Function: typing.ClassVar[SubroutineKind]  # value = <SubroutineKind.Function: 0>
    Task: typing.ClassVar[SubroutineKind]  # value = <SubroutineKind.Task: 1>
    __members__: typing.ClassVar[dict[str, SubroutineKind]]  # value = {'Function': <SubroutineKind.Function: 0>, 'Task': <SubroutineKind.Task: 1>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SubroutineSymbol(Symbol, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arguments(self) -> span[FormalArgumentSymbol]:
        ...
    @property
    def body(self) -> Statement:
        ...
    @property
    def defaultLifetime(self) -> VariableLifetime:
        ...
    @property
    def flags(self) -> MethodFlags:
        ...
    @property
    def isVirtual(self) -> bool:
        ...
    @property
    def override(self) -> SubroutineSymbol:
        ...
    @property
    def prototype(self) -> ...:
        ...
    @property
    def returnType(self) -> ...:
        ...
    @property
    def subroutineKind(self) -> SubroutineKind:
        ...
    @property
    def visibility(self) -> Visibility:
        ...
class SuperNewDefaultedArgsExpressionSyntax(ExpressionSyntax):
    closeParen: Token
    defaultKeyword: Token
    openParen: Token
    scopedNew: NameSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class Symbol:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __repr__(self) -> str:
        ...
    @typing.overload
    def isDeclaredBefore(self, target: Symbol) -> bool | None:
        ...
    @typing.overload
    def isDeclaredBefore(self, location: LookupLocation) -> bool | None:
        ...
    def visit(self, f: typing.Any) -> None:
        """
        Visit a pyslang object with a callback f.

        If f ever returns pyslang.VisitAction.Interrupt, the visit is aborted, and no additional nodes are visited. If f returns pyslang.VisitAction.Skip, then no child nodes of the current node are visited, but otherwise the visit continues. Any other return value, including pslang.VisitAction.Advance is ignored, and the walk continues.
        """
    @property
    def declaredType(self) -> ...:
        ...
    @property
    def declaringDefinition(self) -> ...:
        ...
    @property
    def hierarchicalPath(self) -> str:
        ...
    @property
    def isScope(self) -> bool:
        ...
    @property
    def isType(self) -> bool:
        ...
    @property
    def isValue(self) -> bool:
        ...
    @property
    def kind(self) -> SymbolKind:
        ...
    @property
    def lexicalPath(self) -> str:
        ...
    @property
    def location(self) -> SourceLocation:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def nextSibling(self) -> Symbol:
        ...
    @property
    def parentScope(self) -> ...:
        ...
    @property
    def randMode(self) -> RandMode:
        ...
    @property
    def sourceLibrary(self) -> SourceLibrary:
        ...
    @property
    def syntax(self) -> ...:
        ...
class SymbolKind:
    """
    Members:

      Unknown

      Root

      Definition

      CompilationUnit

      DeferredMember

      TransparentMember

      EmptyMember

      PredefinedIntegerType

      ScalarType

      FloatingType

      EnumType

      EnumValue

      PackedArrayType

      FixedSizeUnpackedArrayType

      DynamicArrayType

      DPIOpenArrayType

      AssociativeArrayType

      QueueType

      PackedStructType

      UnpackedStructType

      PackedUnionType

      UnpackedUnionType

      ClassType

      CovergroupType

      VoidType

      NullType

      CHandleType

      StringType

      EventType

      UnboundedType

      TypeRefType

      UntypedType

      SequenceType

      PropertyType

      VirtualInterfaceType

      TypeAlias

      ErrorType

      ForwardingTypedef

      NetType

      Parameter

      TypeParameter

      Port

      MultiPort

      InterfacePort

      Modport

      ModportPort

      ModportClocking

      Instance

      InstanceBody

      InstanceArray

      Package

      ExplicitImport

      WildcardImport

      Attribute

      Genvar

      GenerateBlock

      GenerateBlockArray

      ProceduralBlock

      StatementBlock

      Net

      Variable

      FormalArgument

      Field

      ClassProperty

      Subroutine

      ContinuousAssign

      ElabSystemTask

      GenericClassDef

      MethodPrototype

      UninstantiatedDef

      Iterator

      PatternVar

      ConstraintBlock

      DefParam

      Specparam

      Primitive

      PrimitivePort

      PrimitiveInstance

      SpecifyBlock

      Sequence

      Property

      AssertionPort

      ClockingBlock

      ClockVar

      LocalAssertionVar

      LetDecl

      Checker

      CheckerInstance

      CheckerInstanceBody

      RandSeqProduction

      CovergroupBody

      Coverpoint

      CoverCross

      CoverCrossBody

      CoverageBin

      TimingPath

      PulseStyle

      SystemTimingCheck

      AnonymousProgram

      NetAlias

      ConfigBlock
    """
    AnonymousProgram: typing.ClassVar[SymbolKind]  # value = <SymbolKind.AnonymousProgram: 98>
    AssertionPort: typing.ClassVar[SymbolKind]  # value = <SymbolKind.AssertionPort: 81>
    AssociativeArrayType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.AssociativeArrayType: 16>
    Attribute: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Attribute: 53>
    CHandleType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CHandleType: 26>
    Checker: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Checker: 86>
    CheckerInstance: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CheckerInstance: 87>
    CheckerInstanceBody: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CheckerInstanceBody: 88>
    ClassProperty: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ClassProperty: 63>
    ClassType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ClassType: 22>
    ClockVar: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ClockVar: 83>
    ClockingBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ClockingBlock: 82>
    CompilationUnit: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CompilationUnit: 3>
    ConfigBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ConfigBlock: 100>
    ConstraintBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ConstraintBlock: 72>
    ContinuousAssign: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ContinuousAssign: 65>
    CoverCross: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CoverCross: 92>
    CoverCrossBody: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CoverCrossBody: 93>
    CoverageBin: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CoverageBin: 94>
    CovergroupBody: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CovergroupBody: 90>
    CovergroupType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CovergroupType: 23>
    Coverpoint: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Coverpoint: 91>
    DPIOpenArrayType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.DPIOpenArrayType: 15>
    DefParam: typing.ClassVar[SymbolKind]  # value = <SymbolKind.DefParam: 73>
    DeferredMember: typing.ClassVar[SymbolKind]  # value = <SymbolKind.DeferredMember: 4>
    Definition: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Definition: 2>
    DynamicArrayType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.DynamicArrayType: 14>
    ElabSystemTask: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ElabSystemTask: 66>
    EmptyMember: typing.ClassVar[SymbolKind]  # value = <SymbolKind.EmptyMember: 6>
    EnumType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.EnumType: 10>
    EnumValue: typing.ClassVar[SymbolKind]  # value = <SymbolKind.EnumValue: 11>
    ErrorType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ErrorType: 36>
    EventType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.EventType: 28>
    ExplicitImport: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ExplicitImport: 51>
    Field: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Field: 62>
    FixedSizeUnpackedArrayType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.FixedSizeUnpackedArrayType: 13>
    FloatingType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.FloatingType: 9>
    FormalArgument: typing.ClassVar[SymbolKind]  # value = <SymbolKind.FormalArgument: 61>
    ForwardingTypedef: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ForwardingTypedef: 37>
    GenerateBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.GenerateBlock: 55>
    GenerateBlockArray: typing.ClassVar[SymbolKind]  # value = <SymbolKind.GenerateBlockArray: 56>
    GenericClassDef: typing.ClassVar[SymbolKind]  # value = <SymbolKind.GenericClassDef: 67>
    Genvar: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Genvar: 54>
    Instance: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Instance: 47>
    InstanceArray: typing.ClassVar[SymbolKind]  # value = <SymbolKind.InstanceArray: 49>
    InstanceBody: typing.ClassVar[SymbolKind]  # value = <SymbolKind.InstanceBody: 48>
    InterfacePort: typing.ClassVar[SymbolKind]  # value = <SymbolKind.InterfacePort: 43>
    Iterator: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Iterator: 70>
    LetDecl: typing.ClassVar[SymbolKind]  # value = <SymbolKind.LetDecl: 85>
    LocalAssertionVar: typing.ClassVar[SymbolKind]  # value = <SymbolKind.LocalAssertionVar: 84>
    MethodPrototype: typing.ClassVar[SymbolKind]  # value = <SymbolKind.MethodPrototype: 68>
    Modport: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Modport: 44>
    ModportClocking: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ModportClocking: 46>
    ModportPort: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ModportPort: 45>
    MultiPort: typing.ClassVar[SymbolKind]  # value = <SymbolKind.MultiPort: 42>
    Net: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Net: 59>
    NetAlias: typing.ClassVar[SymbolKind]  # value = <SymbolKind.NetAlias: 99>
    NetType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.NetType: 38>
    NullType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.NullType: 25>
    Package: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Package: 50>
    PackedArrayType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PackedArrayType: 12>
    PackedStructType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PackedStructType: 18>
    PackedUnionType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PackedUnionType: 20>
    Parameter: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Parameter: 39>
    PatternVar: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PatternVar: 71>
    Port: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Port: 41>
    PredefinedIntegerType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PredefinedIntegerType: 7>
    Primitive: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Primitive: 75>
    PrimitiveInstance: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PrimitiveInstance: 77>
    PrimitivePort: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PrimitivePort: 76>
    ProceduralBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ProceduralBlock: 57>
    Property: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Property: 80>
    PropertyType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PropertyType: 33>
    PulseStyle: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PulseStyle: 96>
    QueueType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.QueueType: 17>
    RandSeqProduction: typing.ClassVar[SymbolKind]  # value = <SymbolKind.RandSeqProduction: 89>
    Root: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Root: 1>
    ScalarType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ScalarType: 8>
    Sequence: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Sequence: 79>
    SequenceType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.SequenceType: 32>
    SpecifyBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.SpecifyBlock: 78>
    Specparam: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Specparam: 74>
    StatementBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.StatementBlock: 58>
    StringType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.StringType: 27>
    Subroutine: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Subroutine: 64>
    SystemTimingCheck: typing.ClassVar[SymbolKind]  # value = <SymbolKind.SystemTimingCheck: 97>
    TimingPath: typing.ClassVar[SymbolKind]  # value = <SymbolKind.TimingPath: 95>
    TransparentMember: typing.ClassVar[SymbolKind]  # value = <SymbolKind.TransparentMember: 5>
    TypeAlias: typing.ClassVar[SymbolKind]  # value = <SymbolKind.TypeAlias: 35>
    TypeParameter: typing.ClassVar[SymbolKind]  # value = <SymbolKind.TypeParameter: 40>
    TypeRefType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.TypeRefType: 30>
    UnboundedType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.UnboundedType: 29>
    UninstantiatedDef: typing.ClassVar[SymbolKind]  # value = <SymbolKind.UninstantiatedDef: 69>
    Unknown: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Unknown: 0>
    UnpackedStructType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.UnpackedStructType: 19>
    UnpackedUnionType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.UnpackedUnionType: 21>
    UntypedType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.UntypedType: 31>
    Variable: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Variable: 60>
    VirtualInterfaceType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.VirtualInterfaceType: 34>
    VoidType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.VoidType: 24>
    WildcardImport: typing.ClassVar[SymbolKind]  # value = <SymbolKind.WildcardImport: 52>
    __members__: typing.ClassVar[dict[str, SymbolKind]]  # value = {'Unknown': <SymbolKind.Unknown: 0>, 'Root': <SymbolKind.Root: 1>, 'Definition': <SymbolKind.Definition: 2>, 'CompilationUnit': <SymbolKind.CompilationUnit: 3>, 'DeferredMember': <SymbolKind.DeferredMember: 4>, 'TransparentMember': <SymbolKind.TransparentMember: 5>, 'EmptyMember': <SymbolKind.EmptyMember: 6>, 'PredefinedIntegerType': <SymbolKind.PredefinedIntegerType: 7>, 'ScalarType': <SymbolKind.ScalarType: 8>, 'FloatingType': <SymbolKind.FloatingType: 9>, 'EnumType': <SymbolKind.EnumType: 10>, 'EnumValue': <SymbolKind.EnumValue: 11>, 'PackedArrayType': <SymbolKind.PackedArrayType: 12>, 'FixedSizeUnpackedArrayType': <SymbolKind.FixedSizeUnpackedArrayType: 13>, 'DynamicArrayType': <SymbolKind.DynamicArrayType: 14>, 'DPIOpenArrayType': <SymbolKind.DPIOpenArrayType: 15>, 'AssociativeArrayType': <SymbolKind.AssociativeArrayType: 16>, 'QueueType': <SymbolKind.QueueType: 17>, 'PackedStructType': <SymbolKind.PackedStructType: 18>, 'UnpackedStructType': <SymbolKind.UnpackedStructType: 19>, 'PackedUnionType': <SymbolKind.PackedUnionType: 20>, 'UnpackedUnionType': <SymbolKind.UnpackedUnionType: 21>, 'ClassType': <SymbolKind.ClassType: 22>, 'CovergroupType': <SymbolKind.CovergroupType: 23>, 'VoidType': <SymbolKind.VoidType: 24>, 'NullType': <SymbolKind.NullType: 25>, 'CHandleType': <SymbolKind.CHandleType: 26>, 'StringType': <SymbolKind.StringType: 27>, 'EventType': <SymbolKind.EventType: 28>, 'UnboundedType': <SymbolKind.UnboundedType: 29>, 'TypeRefType': <SymbolKind.TypeRefType: 30>, 'UntypedType': <SymbolKind.UntypedType: 31>, 'SequenceType': <SymbolKind.SequenceType: 32>, 'PropertyType': <SymbolKind.PropertyType: 33>, 'VirtualInterfaceType': <SymbolKind.VirtualInterfaceType: 34>, 'TypeAlias': <SymbolKind.TypeAlias: 35>, 'ErrorType': <SymbolKind.ErrorType: 36>, 'ForwardingTypedef': <SymbolKind.ForwardingTypedef: 37>, 'NetType': <SymbolKind.NetType: 38>, 'Parameter': <SymbolKind.Parameter: 39>, 'TypeParameter': <SymbolKind.TypeParameter: 40>, 'Port': <SymbolKind.Port: 41>, 'MultiPort': <SymbolKind.MultiPort: 42>, 'InterfacePort': <SymbolKind.InterfacePort: 43>, 'Modport': <SymbolKind.Modport: 44>, 'ModportPort': <SymbolKind.ModportPort: 45>, 'ModportClocking': <SymbolKind.ModportClocking: 46>, 'Instance': <SymbolKind.Instance: 47>, 'InstanceBody': <SymbolKind.InstanceBody: 48>, 'InstanceArray': <SymbolKind.InstanceArray: 49>, 'Package': <SymbolKind.Package: 50>, 'ExplicitImport': <SymbolKind.ExplicitImport: 51>, 'WildcardImport': <SymbolKind.WildcardImport: 52>, 'Attribute': <SymbolKind.Attribute: 53>, 'Genvar': <SymbolKind.Genvar: 54>, 'GenerateBlock': <SymbolKind.GenerateBlock: 55>, 'GenerateBlockArray': <SymbolKind.GenerateBlockArray: 56>, 'ProceduralBlock': <SymbolKind.ProceduralBlock: 57>, 'StatementBlock': <SymbolKind.StatementBlock: 58>, 'Net': <SymbolKind.Net: 59>, 'Variable': <SymbolKind.Variable: 60>, 'FormalArgument': <SymbolKind.FormalArgument: 61>, 'Field': <SymbolKind.Field: 62>, 'ClassProperty': <SymbolKind.ClassProperty: 63>, 'Subroutine': <SymbolKind.Subroutine: 64>, 'ContinuousAssign': <SymbolKind.ContinuousAssign: 65>, 'ElabSystemTask': <SymbolKind.ElabSystemTask: 66>, 'GenericClassDef': <SymbolKind.GenericClassDef: 67>, 'MethodPrototype': <SymbolKind.MethodPrototype: 68>, 'UninstantiatedDef': <SymbolKind.UninstantiatedDef: 69>, 'Iterator': <SymbolKind.Iterator: 70>, 'PatternVar': <SymbolKind.PatternVar: 71>, 'ConstraintBlock': <SymbolKind.ConstraintBlock: 72>, 'DefParam': <SymbolKind.DefParam: 73>, 'Specparam': <SymbolKind.Specparam: 74>, 'Primitive': <SymbolKind.Primitive: 75>, 'PrimitivePort': <SymbolKind.PrimitivePort: 76>, 'PrimitiveInstance': <SymbolKind.PrimitiveInstance: 77>, 'SpecifyBlock': <SymbolKind.SpecifyBlock: 78>, 'Sequence': <SymbolKind.Sequence: 79>, 'Property': <SymbolKind.Property: 80>, 'AssertionPort': <SymbolKind.AssertionPort: 81>, 'ClockingBlock': <SymbolKind.ClockingBlock: 82>, 'ClockVar': <SymbolKind.ClockVar: 83>, 'LocalAssertionVar': <SymbolKind.LocalAssertionVar: 84>, 'LetDecl': <SymbolKind.LetDecl: 85>, 'Checker': <SymbolKind.Checker: 86>, 'CheckerInstance': <SymbolKind.CheckerInstance: 87>, 'CheckerInstanceBody': <SymbolKind.CheckerInstanceBody: 88>, 'RandSeqProduction': <SymbolKind.RandSeqProduction: 89>, 'CovergroupBody': <SymbolKind.CovergroupBody: 90>, 'Coverpoint': <SymbolKind.Coverpoint: 91>, 'CoverCross': <SymbolKind.CoverCross: 92>, 'CoverCrossBody': <SymbolKind.CoverCrossBody: 93>, 'CoverageBin': <SymbolKind.CoverageBin: 94>, 'TimingPath': <SymbolKind.TimingPath: 95>, 'PulseStyle': <SymbolKind.PulseStyle: 96>, 'SystemTimingCheck': <SymbolKind.SystemTimingCheck: 97>, 'AnonymousProgram': <SymbolKind.AnonymousProgram: 98>, 'NetAlias': <SymbolKind.NetAlias: 99>, 'ConfigBlock': <SymbolKind.ConfigBlock: 100>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SyntaxKind:
    """
    Members:

      Unknown

      SyntaxList

      TokenList

      SeparatedList

      AcceptOnPropertyExpr

      ActionBlock

      AddAssignmentExpression

      AddExpression

      AlwaysBlock

      AlwaysCombBlock

      AlwaysFFBlock

      AlwaysLatchBlock

      AndAssignmentExpression

      AndPropertyExpr

      AndSequenceExpr

      AnonymousProgram

      AnsiPortList

      AnsiUdpPortList

      ArgumentList

      ArithmeticLeftShiftAssignmentExpression

      ArithmeticRightShiftAssignmentExpression

      ArithmeticShiftLeftExpression

      ArithmeticShiftRightExpression

      ArrayAndMethod

      ArrayOrMethod

      ArrayOrRandomizeMethodExpression

      ArrayUniqueMethod

      ArrayXorMethod

      AscendingRangeSelect

      AssertPropertyStatement

      AssertionItemPort

      AssertionItemPortList

      AssignmentExpression

      AssignmentPatternExpression

      AssignmentPatternItem

      AssumePropertyStatement

      AttributeInstance

      AttributeSpec

      BadExpression

      BeginKeywordsDirective

      BinSelectWithFilterExpr

      BinaryAndExpression

      BinaryBinsSelectExpr

      BinaryBlockEventExpression

      BinaryConditionalDirectiveExpression

      BinaryEventExpression

      BinaryOrExpression

      BinaryXnorExpression

      BinaryXorExpression

      BindDirective

      BindTargetList

      BinsSelectConditionExpr

      BinsSelection

      BitSelect

      BitType

      BlockCoverageEvent

      BlockingEventTriggerStatement

      ByteType

      CHandleType

      CaseEqualityExpression

      CaseGenerate

      CaseInequalityExpression

      CasePropertyExpr

      CaseStatement

      CastExpression

      CellConfigRule

      CellDefineDirective

      ChargeStrength

      CheckerDataDeclaration

      CheckerDeclaration

      CheckerInstanceStatement

      CheckerInstantiation

      ClassDeclaration

      ClassMethodDeclaration

      ClassMethodPrototype

      ClassName

      ClassPropertyDeclaration

      ClassSpecifier

      ClockingDeclaration

      ClockingDirection

      ClockingItem

      ClockingPropertyExpr

      ClockingSequenceExpr

      ClockingSkew

      ColonExpressionClause

      CompilationUnit

      ConcatenationExpression

      ConcurrentAssertionMember

      ConditionalConstraint

      ConditionalExpression

      ConditionalPathDeclaration

      ConditionalPattern

      ConditionalPredicate

      ConditionalPropertyExpr

      ConditionalStatement

      ConfigCellIdentifier

      ConfigDeclaration

      ConfigInstanceIdentifier

      ConfigLiblist

      ConfigUseClause

      ConstraintBlock

      ConstraintDeclaration

      ConstraintPrototype

      ConstructorName

      ContinuousAssign

      CopyClassExpression

      CoverCross

      CoverPropertyStatement

      CoverSequenceStatement

      CoverageBins

      CoverageBinsArraySize

      CoverageIffClause

      CoverageOption

      CovergroupDeclaration

      Coverpoint

      CycleDelay

      DPIExport

      DPIImport

      DataDeclaration

      Declarator

      DefParam

      DefParamAssignment

      DefaultCaseItem

      DefaultClockingReference

      DefaultConfigRule

      DefaultCoverageBinInitializer

      DefaultDecayTimeDirective

      DefaultDisableDeclaration

      DefaultDistItem

      DefaultExtendsClauseArg

      DefaultFunctionPort

      DefaultNetTypeDirective

      DefaultPatternKeyExpression

      DefaultPropertyCaseItem

      DefaultRsCaseItem

      DefaultSkewItem

      DefaultTriregStrengthDirective

      DeferredAssertion

      DefineDirective

      Delay3

      DelayControl

      DelayModeDistributedDirective

      DelayModePathDirective

      DelayModeUnitDirective

      DelayModeZeroDirective

      DelayedSequenceElement

      DelayedSequenceExpr

      DescendingRangeSelect

      DisableConstraint

      DisableForkStatement

      DisableIff

      DisableStatement

      DistConstraintList

      DistItem

      DistWeight

      DivideAssignmentExpression

      DivideExpression

      DividerClause

      DoWhileStatement

      DotMemberClause

      DriveStrength

      EdgeControlSpecifier

      EdgeDescriptor

      EdgeSensitivePathSuffix

      ElabSystemTask

      ElementSelect

      ElementSelectExpression

      ElsIfDirective

      ElseClause

      ElseConstraintClause

      ElseDirective

      ElsePropertyClause

      EmptyArgument

      EmptyIdentifierName

      EmptyMember

      EmptyNonAnsiPort

      EmptyPortConnection

      EmptyQueueExpression

      EmptyStatement

      EmptyTimingCheckArg

      EndCellDefineDirective

      EndIfDirective

      EndKeywordsDirective

      EndProtectDirective

      EndProtectedDirective

      EnumType

      EqualityExpression

      EqualsAssertionArgClause

      EqualsTypeClause

      EqualsValueClause

      EventControl

      EventControlWithExpression

      EventType

      ExpectPropertyStatement

      ExplicitAnsiPort

      ExplicitNonAnsiPort

      ExpressionConstraint

      ExpressionCoverageBinInitializer

      ExpressionOrDist

      ExpressionPattern

      ExpressionStatement

      ExpressionTimingCheckArg

      ExtendsClause

      ExternInterfaceMethod

      ExternModuleDecl

      ExternUdpDecl

      FilePathSpec

      FinalBlock

      FirstMatchSequenceExpr

      FollowedByPropertyExpr

      ForLoopStatement

      ForVariableDeclaration

      ForeachLoopList

      ForeachLoopStatement

      ForeverStatement

      ForwardTypeRestriction

      ForwardTypedefDeclaration

      FunctionDeclaration

      FunctionPort

      FunctionPortList

      FunctionPrototype

      GenerateBlock

      GenerateRegion

      GenvarDeclaration

      GreaterThanEqualExpression

      GreaterThanExpression

      HierarchicalInstance

      HierarchyInstantiation

      IdWithExprCoverageBinInitializer

      IdentifierName

      IdentifierSelectName

      IfDefDirective

      IfGenerate

      IfNDefDirective

      IfNonePathDeclaration

      IffEventClause

      IffPropertyExpr

      ImmediateAssertStatement

      ImmediateAssertionMember

      ImmediateAssumeStatement

      ImmediateCoverStatement

      ImplementsClause

      ImplicationConstraint

      ImplicationPropertyExpr

      ImplicitAnsiPort

      ImplicitEventControl

      ImplicitNonAnsiPort

      ImplicitType

      ImpliesPropertyExpr

      IncludeDirective

      InequalityExpression

      InitialBlock

      InsideExpression

      InstanceConfigRule

      InstanceName

      IntType

      IntegerLiteralExpression

      IntegerType

      IntegerVectorExpression

      InterfaceDeclaration

      InterfaceHeader

      InterfacePortHeader

      IntersectClause

      IntersectSequenceExpr

      InvocationExpression

      JumpStatement

      LessThanEqualExpression

      LessThanExpression

      LetDeclaration

      LibraryDeclaration

      LibraryIncDirClause

      LibraryIncludeStatement

      LibraryMap

      LineDirective

      LocalScope

      LocalVariableDeclaration

      LogicType

      LogicalAndExpression

      LogicalEquivalenceExpression

      LogicalImplicationExpression

      LogicalLeftShiftAssignmentExpression

      LogicalOrExpression

      LogicalRightShiftAssignmentExpression

      LogicalShiftLeftExpression

      LogicalShiftRightExpression

      LongIntType

      LoopConstraint

      LoopGenerate

      LoopStatement

      MacroActualArgument

      MacroActualArgumentList

      MacroArgumentDefault

      MacroFormalArgument

      MacroFormalArgumentList

      MacroUsage

      MatchesClause

      MemberAccessExpression

      MinTypMaxExpression

      ModAssignmentExpression

      ModExpression

      ModportClockingPort

      ModportDeclaration

      ModportExplicitPort

      ModportItem

      ModportNamedPort

      ModportSimplePortList

      ModportSubroutinePort

      ModportSubroutinePortList

      ModuleDeclaration

      ModuleHeader

      MultipleConcatenationExpression

      MultiplyAssignmentExpression

      MultiplyExpression

      NameValuePragmaExpression

      NamedArgument

      NamedBlockClause

      NamedConditionalDirectiveExpression

      NamedLabel

      NamedParamAssignment

      NamedPortConnection

      NamedStructurePatternMember

      NamedType

      NetAlias

      NetDeclaration

      NetPortHeader

      NetTypeDeclaration

      NewArrayExpression

      NewClassExpression

      NoUnconnectedDriveDirective

      NonAnsiPortList

      NonAnsiUdpPortList

      NonblockingAssignmentExpression

      NonblockingEventTriggerStatement

      NullLiteralExpression

      NumberPragmaExpression

      OneStepDelay

      OrAssignmentExpression

      OrPropertyExpr

      OrSequenceExpr

      OrderedArgument

      OrderedParamAssignment

      OrderedPortConnection

      OrderedStructurePatternMember

      PackageDeclaration

      PackageExportAllDeclaration

      PackageExportDeclaration

      PackageHeader

      PackageImportDeclaration

      PackageImportItem

      ParallelBlockStatement

      ParameterDeclaration

      ParameterDeclarationStatement

      ParameterPortList

      ParameterValueAssignment

      ParenExpressionList

      ParenPragmaExpression

      ParenthesizedBinsSelectExpr

      ParenthesizedConditionalDirectiveExpression

      ParenthesizedEventExpression

      ParenthesizedExpression

      ParenthesizedPattern

      ParenthesizedPropertyExpr

      ParenthesizedSequenceExpr

      PathDeclaration

      PathDescription

      PatternCaseItem

      PortConcatenation

      PortDeclaration

      PortReference

      PostdecrementExpression

      PostincrementExpression

      PowerExpression

      PragmaDirective

      PrimaryBlockEventExpression

      PrimitiveInstantiation

      ProceduralAssignStatement

      ProceduralDeassignStatement

      ProceduralForceStatement

      ProceduralReleaseStatement

      Production

      ProgramDeclaration

      ProgramHeader

      PropertyDeclaration

      PropertySpec

      PropertyType

      ProtectDirective

      ProtectedDirective

      PullStrength

      PulseStyleDeclaration

      QueueDimensionSpecifier

      RandCaseItem

      RandCaseStatement

      RandJoinClause

      RandSequenceStatement

      RangeCoverageBinInitializer

      RangeDimensionSpecifier

      RangeList

      RealLiteralExpression

      RealTimeType

      RealType

      RegType

      RepeatedEventControl

      ReplicatedAssignmentPattern

      ResetAllDirective

      RestrictPropertyStatement

      ReturnStatement

      RootScope

      RsCase

      RsCodeBlock

      RsElseClause

      RsIfElse

      RsProdItem

      RsRepeat

      RsRule

      RsWeightClause

      SUntilPropertyExpr

      SUntilWithPropertyExpr

      ScopedName

      SequenceDeclaration

      SequenceMatchList

      SequenceRepetition

      SequenceType

      SequentialBlockStatement

      ShortIntType

      ShortRealType

      SignalEventExpression

      SignedCastExpression

      SimpleAssignmentPattern

      SimpleBinsSelectExpr

      SimplePathSuffix

      SimplePragmaExpression

      SimplePropertyExpr

      SimpleRangeSelect

      SimpleSequenceExpr

      SolveBeforeConstraint

      SpecifyBlock

      SpecparamDeclaration

      SpecparamDeclarator

      StandardCaseItem

      StandardPropertyCaseItem

      StandardRsCaseItem

      StreamExpression

      StreamExpressionWithRange

      StreamingConcatenationExpression

      StringLiteralExpression

      StringType

      StrongWeakPropertyExpr

      StructType

      StructUnionMember

      StructurePattern

      StructuredAssignmentPattern

      SubtractAssignmentExpression

      SubtractExpression

      SuperHandle

      SuperNewDefaultedArgsExpression

      SystemName

      SystemTimingCheck

      TaggedPattern

      TaggedUnionExpression

      TaskDeclaration

      ThisHandle

      ThroughoutSequenceExpr

      TimeLiteralExpression

      TimeScaleDirective

      TimeType

      TimeUnitsDeclaration

      TimingCheckEventArg

      TimingCheckEventCondition

      TimingControlExpression

      TimingControlStatement

      TransListCoverageBinInitializer

      TransRange

      TransRepeatRange

      TransSet

      TypeAssignment

      TypeParameterDeclaration

      TypeReference

      TypedefDeclaration

      UdpBody

      UdpDeclaration

      UdpEdgeField

      UdpEntry

      UdpInitialStmt

      UdpInputPortDecl

      UdpOutputPortDecl

      UdpSimpleField

      UnaryBinsSelectExpr

      UnaryBitwiseAndExpression

      UnaryBitwiseNandExpression

      UnaryBitwiseNorExpression

      UnaryBitwiseNotExpression

      UnaryBitwiseOrExpression

      UnaryBitwiseXnorExpression

      UnaryBitwiseXorExpression

      UnaryConditionalDirectiveExpression

      UnaryLogicalNotExpression

      UnaryMinusExpression

      UnaryPlusExpression

      UnaryPredecrementExpression

      UnaryPreincrementExpression

      UnaryPropertyExpr

      UnarySelectPropertyExpr

      UnbasedUnsizedLiteralExpression

      UnconnectedDriveDirective

      UndefDirective

      UndefineAllDirective

      UnionType

      UniquenessConstraint

      UnitScope

      UntilPropertyExpr

      UntilWithPropertyExpr

      Untyped

      UserDefinedNetDeclaration

      ValueRangeExpression

      VariableDimension

      VariablePattern

      VariablePortHeader

      VirtualInterfaceType

      VoidCastedCallStatement

      VoidType

      WaitForkStatement

      WaitOrderStatement

      WaitStatement

      WildcardDimensionSpecifier

      WildcardEqualityExpression

      WildcardInequalityExpression

      WildcardLiteralExpression

      WildcardPattern

      WildcardPortConnection

      WildcardPortList

      WildcardUdpPortList

      WithClause

      WithFunctionClause

      WithFunctionSample

      WithinSequenceExpr

      XorAssignmentExpression
    """
    AcceptOnPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AcceptOnPropertyExpr: 4>
    ActionBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ActionBlock: 5>
    AddAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AddAssignmentExpression: 6>
    AddExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AddExpression: 7>
    AlwaysBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AlwaysBlock: 8>
    AlwaysCombBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AlwaysCombBlock: 9>
    AlwaysFFBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AlwaysFFBlock: 10>
    AlwaysLatchBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AlwaysLatchBlock: 11>
    AndAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AndAssignmentExpression: 12>
    AndPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AndPropertyExpr: 13>
    AndSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AndSequenceExpr: 14>
    AnonymousProgram: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AnonymousProgram: 15>
    AnsiPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AnsiPortList: 16>
    AnsiUdpPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AnsiUdpPortList: 17>
    ArgumentList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArgumentList: 18>
    ArithmeticLeftShiftAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArithmeticLeftShiftAssignmentExpression: 19>
    ArithmeticRightShiftAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArithmeticRightShiftAssignmentExpression: 20>
    ArithmeticShiftLeftExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArithmeticShiftLeftExpression: 21>
    ArithmeticShiftRightExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArithmeticShiftRightExpression: 22>
    ArrayAndMethod: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArrayAndMethod: 23>
    ArrayOrMethod: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArrayOrMethod: 24>
    ArrayOrRandomizeMethodExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArrayOrRandomizeMethodExpression: 25>
    ArrayUniqueMethod: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArrayUniqueMethod: 26>
    ArrayXorMethod: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArrayXorMethod: 27>
    AscendingRangeSelect: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AscendingRangeSelect: 28>
    AssertPropertyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssertPropertyStatement: 29>
    AssertionItemPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssertionItemPort: 30>
    AssertionItemPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssertionItemPortList: 31>
    AssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssignmentExpression: 32>
    AssignmentPatternExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssignmentPatternExpression: 33>
    AssignmentPatternItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssignmentPatternItem: 34>
    AssumePropertyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssumePropertyStatement: 35>
    AttributeInstance: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AttributeInstance: 36>
    AttributeSpec: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AttributeSpec: 37>
    BadExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BadExpression: 38>
    BeginKeywordsDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BeginKeywordsDirective: 39>
    BinSelectWithFilterExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinSelectWithFilterExpr: 40>
    BinaryAndExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryAndExpression: 41>
    BinaryBinsSelectExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryBinsSelectExpr: 42>
    BinaryBlockEventExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryBlockEventExpression: 43>
    BinaryConditionalDirectiveExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryConditionalDirectiveExpression: 44>
    BinaryEventExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryEventExpression: 45>
    BinaryOrExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryOrExpression: 46>
    BinaryXnorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryXnorExpression: 47>
    BinaryXorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryXorExpression: 48>
    BindDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BindDirective: 49>
    BindTargetList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BindTargetList: 50>
    BinsSelectConditionExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinsSelectConditionExpr: 51>
    BinsSelection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinsSelection: 52>
    BitSelect: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BitSelect: 53>
    BitType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BitType: 54>
    BlockCoverageEvent: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BlockCoverageEvent: 55>
    BlockingEventTriggerStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BlockingEventTriggerStatement: 56>
    ByteType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ByteType: 57>
    CHandleType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CHandleType: 58>
    CaseEqualityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CaseEqualityExpression: 59>
    CaseGenerate: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CaseGenerate: 60>
    CaseInequalityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CaseInequalityExpression: 61>
    CasePropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CasePropertyExpr: 62>
    CaseStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CaseStatement: 63>
    CastExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CastExpression: 64>
    CellConfigRule: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CellConfigRule: 65>
    CellDefineDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CellDefineDirective: 66>
    ChargeStrength: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ChargeStrength: 67>
    CheckerDataDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CheckerDataDeclaration: 68>
    CheckerDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CheckerDeclaration: 69>
    CheckerInstanceStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CheckerInstanceStatement: 70>
    CheckerInstantiation: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CheckerInstantiation: 71>
    ClassDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassDeclaration: 72>
    ClassMethodDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassMethodDeclaration: 73>
    ClassMethodPrototype: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassMethodPrototype: 74>
    ClassName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassName: 75>
    ClassPropertyDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassPropertyDeclaration: 76>
    ClassSpecifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassSpecifier: 77>
    ClockingDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingDeclaration: 78>
    ClockingDirection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingDirection: 79>
    ClockingItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingItem: 80>
    ClockingPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingPropertyExpr: 81>
    ClockingSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingSequenceExpr: 82>
    ClockingSkew: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingSkew: 83>
    ColonExpressionClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ColonExpressionClause: 84>
    CompilationUnit: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CompilationUnit: 85>
    ConcatenationExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConcatenationExpression: 86>
    ConcurrentAssertionMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConcurrentAssertionMember: 87>
    ConditionalConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalConstraint: 88>
    ConditionalExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalExpression: 89>
    ConditionalPathDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalPathDeclaration: 90>
    ConditionalPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalPattern: 91>
    ConditionalPredicate: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalPredicate: 92>
    ConditionalPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalPropertyExpr: 93>
    ConditionalStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalStatement: 94>
    ConfigCellIdentifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConfigCellIdentifier: 95>
    ConfigDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConfigDeclaration: 96>
    ConfigInstanceIdentifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConfigInstanceIdentifier: 97>
    ConfigLiblist: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConfigLiblist: 98>
    ConfigUseClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConfigUseClause: 99>
    ConstraintBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConstraintBlock: 100>
    ConstraintDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConstraintDeclaration: 101>
    ConstraintPrototype: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConstraintPrototype: 102>
    ConstructorName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConstructorName: 103>
    ContinuousAssign: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ContinuousAssign: 104>
    CopyClassExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CopyClassExpression: 105>
    CoverCross: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverCross: 106>
    CoverPropertyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverPropertyStatement: 107>
    CoverSequenceStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverSequenceStatement: 108>
    CoverageBins: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverageBins: 109>
    CoverageBinsArraySize: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverageBinsArraySize: 110>
    CoverageIffClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverageIffClause: 111>
    CoverageOption: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverageOption: 112>
    CovergroupDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CovergroupDeclaration: 113>
    Coverpoint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Coverpoint: 114>
    CycleDelay: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CycleDelay: 115>
    DPIExport: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DPIExport: 116>
    DPIImport: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DPIImport: 117>
    DataDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DataDeclaration: 118>
    Declarator: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Declarator: 119>
    DefParam: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefParam: 120>
    DefParamAssignment: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefParamAssignment: 121>
    DefaultCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultCaseItem: 122>
    DefaultClockingReference: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultClockingReference: 123>
    DefaultConfigRule: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultConfigRule: 124>
    DefaultCoverageBinInitializer: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultCoverageBinInitializer: 125>
    DefaultDecayTimeDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultDecayTimeDirective: 126>
    DefaultDisableDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultDisableDeclaration: 127>
    DefaultDistItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultDistItem: 128>
    DefaultExtendsClauseArg: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultExtendsClauseArg: 129>
    DefaultFunctionPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultFunctionPort: 130>
    DefaultNetTypeDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultNetTypeDirective: 131>
    DefaultPatternKeyExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultPatternKeyExpression: 132>
    DefaultPropertyCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultPropertyCaseItem: 133>
    DefaultRsCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultRsCaseItem: 134>
    DefaultSkewItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultSkewItem: 135>
    DefaultTriregStrengthDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultTriregStrengthDirective: 136>
    DeferredAssertion: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DeferredAssertion: 137>
    DefineDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefineDirective: 138>
    Delay3: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Delay3: 139>
    DelayControl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DelayControl: 140>
    DelayModeDistributedDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DelayModeDistributedDirective: 141>
    DelayModePathDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DelayModePathDirective: 142>
    DelayModeUnitDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DelayModeUnitDirective: 143>
    DelayModeZeroDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DelayModeZeroDirective: 144>
    DelayedSequenceElement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DelayedSequenceElement: 145>
    DelayedSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DelayedSequenceExpr: 146>
    DescendingRangeSelect: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DescendingRangeSelect: 147>
    DisableConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DisableConstraint: 148>
    DisableForkStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DisableForkStatement: 149>
    DisableIff: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DisableIff: 150>
    DisableStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DisableStatement: 151>
    DistConstraintList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DistConstraintList: 152>
    DistItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DistItem: 153>
    DistWeight: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DistWeight: 154>
    DivideAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DivideAssignmentExpression: 155>
    DivideExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DivideExpression: 156>
    DividerClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DividerClause: 157>
    DoWhileStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DoWhileStatement: 158>
    DotMemberClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DotMemberClause: 159>
    DriveStrength: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DriveStrength: 160>
    EdgeControlSpecifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EdgeControlSpecifier: 161>
    EdgeDescriptor: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EdgeDescriptor: 162>
    EdgeSensitivePathSuffix: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EdgeSensitivePathSuffix: 163>
    ElabSystemTask: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElabSystemTask: 164>
    ElementSelect: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElementSelect: 165>
    ElementSelectExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElementSelectExpression: 166>
    ElsIfDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElsIfDirective: 167>
    ElseClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElseClause: 168>
    ElseConstraintClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElseConstraintClause: 169>
    ElseDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElseDirective: 170>
    ElsePropertyClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElsePropertyClause: 171>
    EmptyArgument: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyArgument: 172>
    EmptyIdentifierName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyIdentifierName: 173>
    EmptyMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyMember: 174>
    EmptyNonAnsiPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyNonAnsiPort: 175>
    EmptyPortConnection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyPortConnection: 176>
    EmptyQueueExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyQueueExpression: 177>
    EmptyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyStatement: 178>
    EmptyTimingCheckArg: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyTimingCheckArg: 179>
    EndCellDefineDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EndCellDefineDirective: 180>
    EndIfDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EndIfDirective: 181>
    EndKeywordsDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EndKeywordsDirective: 182>
    EndProtectDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EndProtectDirective: 183>
    EndProtectedDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EndProtectedDirective: 184>
    EnumType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EnumType: 185>
    EqualityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EqualityExpression: 186>
    EqualsAssertionArgClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EqualsAssertionArgClause: 187>
    EqualsTypeClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EqualsTypeClause: 188>
    EqualsValueClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EqualsValueClause: 189>
    EventControl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EventControl: 190>
    EventControlWithExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EventControlWithExpression: 191>
    EventType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EventType: 192>
    ExpectPropertyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpectPropertyStatement: 193>
    ExplicitAnsiPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExplicitAnsiPort: 194>
    ExplicitNonAnsiPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExplicitNonAnsiPort: 195>
    ExpressionConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionConstraint: 196>
    ExpressionCoverageBinInitializer: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionCoverageBinInitializer: 197>
    ExpressionOrDist: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionOrDist: 198>
    ExpressionPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionPattern: 199>
    ExpressionStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionStatement: 200>
    ExpressionTimingCheckArg: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionTimingCheckArg: 201>
    ExtendsClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExtendsClause: 202>
    ExternInterfaceMethod: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExternInterfaceMethod: 203>
    ExternModuleDecl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExternModuleDecl: 204>
    ExternUdpDecl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExternUdpDecl: 205>
    FilePathSpec: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FilePathSpec: 206>
    FinalBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FinalBlock: 207>
    FirstMatchSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FirstMatchSequenceExpr: 208>
    FollowedByPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FollowedByPropertyExpr: 209>
    ForLoopStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForLoopStatement: 210>
    ForVariableDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForVariableDeclaration: 211>
    ForeachLoopList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForeachLoopList: 212>
    ForeachLoopStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForeachLoopStatement: 213>
    ForeverStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForeverStatement: 214>
    ForwardTypeRestriction: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForwardTypeRestriction: 215>
    ForwardTypedefDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForwardTypedefDeclaration: 216>
    FunctionDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FunctionDeclaration: 217>
    FunctionPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FunctionPort: 218>
    FunctionPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FunctionPortList: 219>
    FunctionPrototype: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FunctionPrototype: 220>
    GenerateBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.GenerateBlock: 221>
    GenerateRegion: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.GenerateRegion: 222>
    GenvarDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.GenvarDeclaration: 223>
    GreaterThanEqualExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.GreaterThanEqualExpression: 224>
    GreaterThanExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.GreaterThanExpression: 225>
    HierarchicalInstance: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.HierarchicalInstance: 226>
    HierarchyInstantiation: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.HierarchyInstantiation: 227>
    IdWithExprCoverageBinInitializer: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IdWithExprCoverageBinInitializer: 228>
    IdentifierName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IdentifierName: 229>
    IdentifierSelectName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IdentifierSelectName: 230>
    IfDefDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IfDefDirective: 231>
    IfGenerate: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IfGenerate: 232>
    IfNDefDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IfNDefDirective: 233>
    IfNonePathDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IfNonePathDeclaration: 234>
    IffEventClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IffEventClause: 235>
    IffPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IffPropertyExpr: 236>
    ImmediateAssertStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImmediateAssertStatement: 237>
    ImmediateAssertionMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImmediateAssertionMember: 238>
    ImmediateAssumeStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImmediateAssumeStatement: 239>
    ImmediateCoverStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImmediateCoverStatement: 240>
    ImplementsClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplementsClause: 241>
    ImplicationConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicationConstraint: 242>
    ImplicationPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicationPropertyExpr: 243>
    ImplicitAnsiPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicitAnsiPort: 244>
    ImplicitEventControl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicitEventControl: 245>
    ImplicitNonAnsiPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicitNonAnsiPort: 246>
    ImplicitType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicitType: 247>
    ImpliesPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImpliesPropertyExpr: 248>
    IncludeDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IncludeDirective: 249>
    InequalityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InequalityExpression: 250>
    InitialBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InitialBlock: 251>
    InsideExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InsideExpression: 252>
    InstanceConfigRule: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InstanceConfigRule: 253>
    InstanceName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InstanceName: 254>
    IntType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntType: 255>
    IntegerLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntegerLiteralExpression: 256>
    IntegerType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntegerType: 257>
    IntegerVectorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntegerVectorExpression: 258>
    InterfaceDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InterfaceDeclaration: 259>
    InterfaceHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InterfaceHeader: 260>
    InterfacePortHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InterfacePortHeader: 261>
    IntersectClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntersectClause: 262>
    IntersectSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntersectSequenceExpr: 263>
    InvocationExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InvocationExpression: 264>
    JumpStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.JumpStatement: 265>
    LessThanEqualExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LessThanEqualExpression: 266>
    LessThanExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LessThanExpression: 267>
    LetDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LetDeclaration: 268>
    LibraryDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LibraryDeclaration: 269>
    LibraryIncDirClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LibraryIncDirClause: 270>
    LibraryIncludeStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LibraryIncludeStatement: 271>
    LibraryMap: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LibraryMap: 272>
    LineDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LineDirective: 273>
    LocalScope: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LocalScope: 274>
    LocalVariableDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LocalVariableDeclaration: 275>
    LogicType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicType: 276>
    LogicalAndExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalAndExpression: 277>
    LogicalEquivalenceExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalEquivalenceExpression: 278>
    LogicalImplicationExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalImplicationExpression: 279>
    LogicalLeftShiftAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalLeftShiftAssignmentExpression: 280>
    LogicalOrExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalOrExpression: 281>
    LogicalRightShiftAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalRightShiftAssignmentExpression: 282>
    LogicalShiftLeftExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalShiftLeftExpression: 283>
    LogicalShiftRightExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalShiftRightExpression: 284>
    LongIntType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LongIntType: 285>
    LoopConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LoopConstraint: 286>
    LoopGenerate: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LoopGenerate: 287>
    LoopStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LoopStatement: 288>
    MacroActualArgument: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroActualArgument: 289>
    MacroActualArgumentList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroActualArgumentList: 290>
    MacroArgumentDefault: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroArgumentDefault: 291>
    MacroFormalArgument: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroFormalArgument: 292>
    MacroFormalArgumentList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroFormalArgumentList: 293>
    MacroUsage: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroUsage: 294>
    MatchesClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MatchesClause: 295>
    MemberAccessExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MemberAccessExpression: 296>
    MinTypMaxExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MinTypMaxExpression: 297>
    ModAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModAssignmentExpression: 298>
    ModExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModExpression: 299>
    ModportClockingPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportClockingPort: 300>
    ModportDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportDeclaration: 301>
    ModportExplicitPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportExplicitPort: 302>
    ModportItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportItem: 303>
    ModportNamedPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportNamedPort: 304>
    ModportSimplePortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportSimplePortList: 305>
    ModportSubroutinePort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportSubroutinePort: 306>
    ModportSubroutinePortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportSubroutinePortList: 307>
    ModuleDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModuleDeclaration: 308>
    ModuleHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModuleHeader: 309>
    MultipleConcatenationExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MultipleConcatenationExpression: 310>
    MultiplyAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MultiplyAssignmentExpression: 311>
    MultiplyExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MultiplyExpression: 312>
    NameValuePragmaExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NameValuePragmaExpression: 313>
    NamedArgument: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedArgument: 314>
    NamedBlockClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedBlockClause: 315>
    NamedConditionalDirectiveExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedConditionalDirectiveExpression: 316>
    NamedLabel: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedLabel: 317>
    NamedParamAssignment: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedParamAssignment: 318>
    NamedPortConnection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedPortConnection: 319>
    NamedStructurePatternMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedStructurePatternMember: 320>
    NamedType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedType: 321>
    NetAlias: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NetAlias: 322>
    NetDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NetDeclaration: 323>
    NetPortHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NetPortHeader: 324>
    NetTypeDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NetTypeDeclaration: 325>
    NewArrayExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NewArrayExpression: 326>
    NewClassExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NewClassExpression: 327>
    NoUnconnectedDriveDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NoUnconnectedDriveDirective: 328>
    NonAnsiPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NonAnsiPortList: 329>
    NonAnsiUdpPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NonAnsiUdpPortList: 330>
    NonblockingAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NonblockingAssignmentExpression: 331>
    NonblockingEventTriggerStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NonblockingEventTriggerStatement: 332>
    NullLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NullLiteralExpression: 333>
    NumberPragmaExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NumberPragmaExpression: 334>
    OneStepDelay: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OneStepDelay: 335>
    OrAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrAssignmentExpression: 336>
    OrPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrPropertyExpr: 337>
    OrSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrSequenceExpr: 338>
    OrderedArgument: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrderedArgument: 339>
    OrderedParamAssignment: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrderedParamAssignment: 340>
    OrderedPortConnection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrderedPortConnection: 341>
    OrderedStructurePatternMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrderedStructurePatternMember: 342>
    PackageDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageDeclaration: 343>
    PackageExportAllDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageExportAllDeclaration: 344>
    PackageExportDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageExportDeclaration: 345>
    PackageHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageHeader: 346>
    PackageImportDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageImportDeclaration: 347>
    PackageImportItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageImportItem: 348>
    ParallelBlockStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParallelBlockStatement: 349>
    ParameterDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParameterDeclaration: 350>
    ParameterDeclarationStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParameterDeclarationStatement: 351>
    ParameterPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParameterPortList: 352>
    ParameterValueAssignment: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParameterValueAssignment: 353>
    ParenExpressionList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenExpressionList: 354>
    ParenPragmaExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenPragmaExpression: 355>
    ParenthesizedBinsSelectExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedBinsSelectExpr: 356>
    ParenthesizedConditionalDirectiveExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedConditionalDirectiveExpression: 357>
    ParenthesizedEventExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedEventExpression: 358>
    ParenthesizedExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedExpression: 359>
    ParenthesizedPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedPattern: 360>
    ParenthesizedPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedPropertyExpr: 361>
    ParenthesizedSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedSequenceExpr: 362>
    PathDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PathDeclaration: 363>
    PathDescription: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PathDescription: 364>
    PatternCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PatternCaseItem: 365>
    PortConcatenation: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PortConcatenation: 366>
    PortDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PortDeclaration: 367>
    PortReference: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PortReference: 368>
    PostdecrementExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PostdecrementExpression: 369>
    PostincrementExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PostincrementExpression: 370>
    PowerExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PowerExpression: 371>
    PragmaDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PragmaDirective: 372>
    PrimaryBlockEventExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PrimaryBlockEventExpression: 373>
    PrimitiveInstantiation: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PrimitiveInstantiation: 374>
    ProceduralAssignStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProceduralAssignStatement: 375>
    ProceduralDeassignStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProceduralDeassignStatement: 376>
    ProceduralForceStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProceduralForceStatement: 377>
    ProceduralReleaseStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProceduralReleaseStatement: 378>
    Production: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Production: 379>
    ProgramDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProgramDeclaration: 380>
    ProgramHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProgramHeader: 381>
    PropertyDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PropertyDeclaration: 382>
    PropertySpec: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PropertySpec: 383>
    PropertyType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PropertyType: 384>
    ProtectDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProtectDirective: 385>
    ProtectedDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProtectedDirective: 386>
    PullStrength: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PullStrength: 387>
    PulseStyleDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PulseStyleDeclaration: 388>
    QueueDimensionSpecifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.QueueDimensionSpecifier: 389>
    RandCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RandCaseItem: 390>
    RandCaseStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RandCaseStatement: 391>
    RandJoinClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RandJoinClause: 392>
    RandSequenceStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RandSequenceStatement: 393>
    RangeCoverageBinInitializer: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RangeCoverageBinInitializer: 394>
    RangeDimensionSpecifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RangeDimensionSpecifier: 395>
    RangeList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RangeList: 396>
    RealLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RealLiteralExpression: 397>
    RealTimeType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RealTimeType: 398>
    RealType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RealType: 399>
    RegType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RegType: 400>
    RepeatedEventControl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RepeatedEventControl: 401>
    ReplicatedAssignmentPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ReplicatedAssignmentPattern: 402>
    ResetAllDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ResetAllDirective: 403>
    RestrictPropertyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RestrictPropertyStatement: 404>
    ReturnStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ReturnStatement: 405>
    RootScope: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RootScope: 406>
    RsCase: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsCase: 407>
    RsCodeBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsCodeBlock: 408>
    RsElseClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsElseClause: 409>
    RsIfElse: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsIfElse: 410>
    RsProdItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsProdItem: 411>
    RsRepeat: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsRepeat: 412>
    RsRule: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsRule: 413>
    RsWeightClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsWeightClause: 414>
    SUntilPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SUntilPropertyExpr: 415>
    SUntilWithPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SUntilWithPropertyExpr: 416>
    ScopedName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ScopedName: 417>
    SeparatedList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SeparatedList: 3>
    SequenceDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SequenceDeclaration: 418>
    SequenceMatchList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SequenceMatchList: 419>
    SequenceRepetition: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SequenceRepetition: 420>
    SequenceType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SequenceType: 421>
    SequentialBlockStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SequentialBlockStatement: 422>
    ShortIntType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ShortIntType: 423>
    ShortRealType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ShortRealType: 424>
    SignalEventExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SignalEventExpression: 425>
    SignedCastExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SignedCastExpression: 426>
    SimpleAssignmentPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimpleAssignmentPattern: 427>
    SimpleBinsSelectExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimpleBinsSelectExpr: 428>
    SimplePathSuffix: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimplePathSuffix: 429>
    SimplePragmaExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimplePragmaExpression: 430>
    SimplePropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimplePropertyExpr: 431>
    SimpleRangeSelect: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimpleRangeSelect: 432>
    SimpleSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimpleSequenceExpr: 433>
    SolveBeforeConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SolveBeforeConstraint: 434>
    SpecifyBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SpecifyBlock: 435>
    SpecparamDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SpecparamDeclaration: 436>
    SpecparamDeclarator: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SpecparamDeclarator: 437>
    StandardCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StandardCaseItem: 438>
    StandardPropertyCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StandardPropertyCaseItem: 439>
    StandardRsCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StandardRsCaseItem: 440>
    StreamExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StreamExpression: 441>
    StreamExpressionWithRange: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StreamExpressionWithRange: 442>
    StreamingConcatenationExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StreamingConcatenationExpression: 443>
    StringLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StringLiteralExpression: 444>
    StringType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StringType: 445>
    StrongWeakPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StrongWeakPropertyExpr: 446>
    StructType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StructType: 447>
    StructUnionMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StructUnionMember: 448>
    StructurePattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StructurePattern: 449>
    StructuredAssignmentPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StructuredAssignmentPattern: 450>
    SubtractAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SubtractAssignmentExpression: 451>
    SubtractExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SubtractExpression: 452>
    SuperHandle: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SuperHandle: 453>
    SuperNewDefaultedArgsExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SuperNewDefaultedArgsExpression: 454>
    SyntaxList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SyntaxList: 1>
    SystemName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SystemName: 455>
    SystemTimingCheck: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SystemTimingCheck: 456>
    TaggedPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TaggedPattern: 457>
    TaggedUnionExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TaggedUnionExpression: 458>
    TaskDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TaskDeclaration: 459>
    ThisHandle: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ThisHandle: 460>
    ThroughoutSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ThroughoutSequenceExpr: 461>
    TimeLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimeLiteralExpression: 462>
    TimeScaleDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimeScaleDirective: 463>
    TimeType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimeType: 464>
    TimeUnitsDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimeUnitsDeclaration: 465>
    TimingCheckEventArg: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimingCheckEventArg: 466>
    TimingCheckEventCondition: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimingCheckEventCondition: 467>
    TimingControlExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimingControlExpression: 468>
    TimingControlStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimingControlStatement: 469>
    TokenList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TokenList: 2>
    TransListCoverageBinInitializer: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TransListCoverageBinInitializer: 470>
    TransRange: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TransRange: 471>
    TransRepeatRange: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TransRepeatRange: 472>
    TransSet: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TransSet: 473>
    TypeAssignment: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TypeAssignment: 474>
    TypeParameterDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TypeParameterDeclaration: 475>
    TypeReference: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TypeReference: 476>
    TypedefDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TypedefDeclaration: 477>
    UdpBody: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpBody: 478>
    UdpDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpDeclaration: 479>
    UdpEdgeField: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpEdgeField: 480>
    UdpEntry: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpEntry: 481>
    UdpInitialStmt: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpInitialStmt: 482>
    UdpInputPortDecl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpInputPortDecl: 483>
    UdpOutputPortDecl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpOutputPortDecl: 484>
    UdpSimpleField: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpSimpleField: 485>
    UnaryBinsSelectExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBinsSelectExpr: 486>
    UnaryBitwiseAndExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseAndExpression: 487>
    UnaryBitwiseNandExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseNandExpression: 488>
    UnaryBitwiseNorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseNorExpression: 489>
    UnaryBitwiseNotExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseNotExpression: 490>
    UnaryBitwiseOrExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseOrExpression: 491>
    UnaryBitwiseXnorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseXnorExpression: 492>
    UnaryBitwiseXorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseXorExpression: 493>
    UnaryConditionalDirectiveExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryConditionalDirectiveExpression: 494>
    UnaryLogicalNotExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryLogicalNotExpression: 495>
    UnaryMinusExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryMinusExpression: 496>
    UnaryPlusExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryPlusExpression: 497>
    UnaryPredecrementExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryPredecrementExpression: 498>
    UnaryPreincrementExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryPreincrementExpression: 499>
    UnaryPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryPropertyExpr: 500>
    UnarySelectPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnarySelectPropertyExpr: 501>
    UnbasedUnsizedLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnbasedUnsizedLiteralExpression: 502>
    UnconnectedDriveDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnconnectedDriveDirective: 503>
    UndefDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UndefDirective: 504>
    UndefineAllDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UndefineAllDirective: 505>
    UnionType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnionType: 506>
    UniquenessConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UniquenessConstraint: 507>
    UnitScope: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnitScope: 508>
    Unknown: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Unknown: 0>
    UntilPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UntilPropertyExpr: 509>
    UntilWithPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UntilWithPropertyExpr: 510>
    Untyped: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Untyped: 511>
    UserDefinedNetDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UserDefinedNetDeclaration: 512>
    ValueRangeExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ValueRangeExpression: 513>
    VariableDimension: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VariableDimension: 514>
    VariablePattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VariablePattern: 515>
    VariablePortHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VariablePortHeader: 516>
    VirtualInterfaceType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VirtualInterfaceType: 517>
    VoidCastedCallStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VoidCastedCallStatement: 518>
    VoidType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VoidType: 519>
    WaitForkStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WaitForkStatement: 520>
    WaitOrderStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WaitOrderStatement: 521>
    WaitStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WaitStatement: 522>
    WildcardDimensionSpecifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardDimensionSpecifier: 523>
    WildcardEqualityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardEqualityExpression: 524>
    WildcardInequalityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardInequalityExpression: 525>
    WildcardLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardLiteralExpression: 526>
    WildcardPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardPattern: 527>
    WildcardPortConnection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardPortConnection: 528>
    WildcardPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardPortList: 529>
    WildcardUdpPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardUdpPortList: 530>
    WithClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WithClause: 531>
    WithFunctionClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WithFunctionClause: 532>
    WithFunctionSample: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WithFunctionSample: 533>
    WithinSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WithinSequenceExpr: 534>
    XorAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.XorAssignmentExpression: 535>
    __members__: typing.ClassVar[dict[str, SyntaxKind]]  # value = {'Unknown': <SyntaxKind.Unknown: 0>, 'SyntaxList': <SyntaxKind.SyntaxList: 1>, 'TokenList': <SyntaxKind.TokenList: 2>, 'SeparatedList': <SyntaxKind.SeparatedList: 3>, 'AcceptOnPropertyExpr': <SyntaxKind.AcceptOnPropertyExpr: 4>, 'ActionBlock': <SyntaxKind.ActionBlock: 5>, 'AddAssignmentExpression': <SyntaxKind.AddAssignmentExpression: 6>, 'AddExpression': <SyntaxKind.AddExpression: 7>, 'AlwaysBlock': <SyntaxKind.AlwaysBlock: 8>, 'AlwaysCombBlock': <SyntaxKind.AlwaysCombBlock: 9>, 'AlwaysFFBlock': <SyntaxKind.AlwaysFFBlock: 10>, 'AlwaysLatchBlock': <SyntaxKind.AlwaysLatchBlock: 11>, 'AndAssignmentExpression': <SyntaxKind.AndAssignmentExpression: 12>, 'AndPropertyExpr': <SyntaxKind.AndPropertyExpr: 13>, 'AndSequenceExpr': <SyntaxKind.AndSequenceExpr: 14>, 'AnonymousProgram': <SyntaxKind.AnonymousProgram: 15>, 'AnsiPortList': <SyntaxKind.AnsiPortList: 16>, 'AnsiUdpPortList': <SyntaxKind.AnsiUdpPortList: 17>, 'ArgumentList': <SyntaxKind.ArgumentList: 18>, 'ArithmeticLeftShiftAssignmentExpression': <SyntaxKind.ArithmeticLeftShiftAssignmentExpression: 19>, 'ArithmeticRightShiftAssignmentExpression': <SyntaxKind.ArithmeticRightShiftAssignmentExpression: 20>, 'ArithmeticShiftLeftExpression': <SyntaxKind.ArithmeticShiftLeftExpression: 21>, 'ArithmeticShiftRightExpression': <SyntaxKind.ArithmeticShiftRightExpression: 22>, 'ArrayAndMethod': <SyntaxKind.ArrayAndMethod: 23>, 'ArrayOrMethod': <SyntaxKind.ArrayOrMethod: 24>, 'ArrayOrRandomizeMethodExpression': <SyntaxKind.ArrayOrRandomizeMethodExpression: 25>, 'ArrayUniqueMethod': <SyntaxKind.ArrayUniqueMethod: 26>, 'ArrayXorMethod': <SyntaxKind.ArrayXorMethod: 27>, 'AscendingRangeSelect': <SyntaxKind.AscendingRangeSelect: 28>, 'AssertPropertyStatement': <SyntaxKind.AssertPropertyStatement: 29>, 'AssertionItemPort': <SyntaxKind.AssertionItemPort: 30>, 'AssertionItemPortList': <SyntaxKind.AssertionItemPortList: 31>, 'AssignmentExpression': <SyntaxKind.AssignmentExpression: 32>, 'AssignmentPatternExpression': <SyntaxKind.AssignmentPatternExpression: 33>, 'AssignmentPatternItem': <SyntaxKind.AssignmentPatternItem: 34>, 'AssumePropertyStatement': <SyntaxKind.AssumePropertyStatement: 35>, 'AttributeInstance': <SyntaxKind.AttributeInstance: 36>, 'AttributeSpec': <SyntaxKind.AttributeSpec: 37>, 'BadExpression': <SyntaxKind.BadExpression: 38>, 'BeginKeywordsDirective': <SyntaxKind.BeginKeywordsDirective: 39>, 'BinSelectWithFilterExpr': <SyntaxKind.BinSelectWithFilterExpr: 40>, 'BinaryAndExpression': <SyntaxKind.BinaryAndExpression: 41>, 'BinaryBinsSelectExpr': <SyntaxKind.BinaryBinsSelectExpr: 42>, 'BinaryBlockEventExpression': <SyntaxKind.BinaryBlockEventExpression: 43>, 'BinaryConditionalDirectiveExpression': <SyntaxKind.BinaryConditionalDirectiveExpression: 44>, 'BinaryEventExpression': <SyntaxKind.BinaryEventExpression: 45>, 'BinaryOrExpression': <SyntaxKind.BinaryOrExpression: 46>, 'BinaryXnorExpression': <SyntaxKind.BinaryXnorExpression: 47>, 'BinaryXorExpression': <SyntaxKind.BinaryXorExpression: 48>, 'BindDirective': <SyntaxKind.BindDirective: 49>, 'BindTargetList': <SyntaxKind.BindTargetList: 50>, 'BinsSelectConditionExpr': <SyntaxKind.BinsSelectConditionExpr: 51>, 'BinsSelection': <SyntaxKind.BinsSelection: 52>, 'BitSelect': <SyntaxKind.BitSelect: 53>, 'BitType': <SyntaxKind.BitType: 54>, 'BlockCoverageEvent': <SyntaxKind.BlockCoverageEvent: 55>, 'BlockingEventTriggerStatement': <SyntaxKind.BlockingEventTriggerStatement: 56>, 'ByteType': <SyntaxKind.ByteType: 57>, 'CHandleType': <SyntaxKind.CHandleType: 58>, 'CaseEqualityExpression': <SyntaxKind.CaseEqualityExpression: 59>, 'CaseGenerate': <SyntaxKind.CaseGenerate: 60>, 'CaseInequalityExpression': <SyntaxKind.CaseInequalityExpression: 61>, 'CasePropertyExpr': <SyntaxKind.CasePropertyExpr: 62>, 'CaseStatement': <SyntaxKind.CaseStatement: 63>, 'CastExpression': <SyntaxKind.CastExpression: 64>, 'CellConfigRule': <SyntaxKind.CellConfigRule: 65>, 'CellDefineDirective': <SyntaxKind.CellDefineDirective: 66>, 'ChargeStrength': <SyntaxKind.ChargeStrength: 67>, 'CheckerDataDeclaration': <SyntaxKind.CheckerDataDeclaration: 68>, 'CheckerDeclaration': <SyntaxKind.CheckerDeclaration: 69>, 'CheckerInstanceStatement': <SyntaxKind.CheckerInstanceStatement: 70>, 'CheckerInstantiation': <SyntaxKind.CheckerInstantiation: 71>, 'ClassDeclaration': <SyntaxKind.ClassDeclaration: 72>, 'ClassMethodDeclaration': <SyntaxKind.ClassMethodDeclaration: 73>, 'ClassMethodPrototype': <SyntaxKind.ClassMethodPrototype: 74>, 'ClassName': <SyntaxKind.ClassName: 75>, 'ClassPropertyDeclaration': <SyntaxKind.ClassPropertyDeclaration: 76>, 'ClassSpecifier': <SyntaxKind.ClassSpecifier: 77>, 'ClockingDeclaration': <SyntaxKind.ClockingDeclaration: 78>, 'ClockingDirection': <SyntaxKind.ClockingDirection: 79>, 'ClockingItem': <SyntaxKind.ClockingItem: 80>, 'ClockingPropertyExpr': <SyntaxKind.ClockingPropertyExpr: 81>, 'ClockingSequenceExpr': <SyntaxKind.ClockingSequenceExpr: 82>, 'ClockingSkew': <SyntaxKind.ClockingSkew: 83>, 'ColonExpressionClause': <SyntaxKind.ColonExpressionClause: 84>, 'CompilationUnit': <SyntaxKind.CompilationUnit: 85>, 'ConcatenationExpression': <SyntaxKind.ConcatenationExpression: 86>, 'ConcurrentAssertionMember': <SyntaxKind.ConcurrentAssertionMember: 87>, 'ConditionalConstraint': <SyntaxKind.ConditionalConstraint: 88>, 'ConditionalExpression': <SyntaxKind.ConditionalExpression: 89>, 'ConditionalPathDeclaration': <SyntaxKind.ConditionalPathDeclaration: 90>, 'ConditionalPattern': <SyntaxKind.ConditionalPattern: 91>, 'ConditionalPredicate': <SyntaxKind.ConditionalPredicate: 92>, 'ConditionalPropertyExpr': <SyntaxKind.ConditionalPropertyExpr: 93>, 'ConditionalStatement': <SyntaxKind.ConditionalStatement: 94>, 'ConfigCellIdentifier': <SyntaxKind.ConfigCellIdentifier: 95>, 'ConfigDeclaration': <SyntaxKind.ConfigDeclaration: 96>, 'ConfigInstanceIdentifier': <SyntaxKind.ConfigInstanceIdentifier: 97>, 'ConfigLiblist': <SyntaxKind.ConfigLiblist: 98>, 'ConfigUseClause': <SyntaxKind.ConfigUseClause: 99>, 'ConstraintBlock': <SyntaxKind.ConstraintBlock: 100>, 'ConstraintDeclaration': <SyntaxKind.ConstraintDeclaration: 101>, 'ConstraintPrototype': <SyntaxKind.ConstraintPrototype: 102>, 'ConstructorName': <SyntaxKind.ConstructorName: 103>, 'ContinuousAssign': <SyntaxKind.ContinuousAssign: 104>, 'CopyClassExpression': <SyntaxKind.CopyClassExpression: 105>, 'CoverCross': <SyntaxKind.CoverCross: 106>, 'CoverPropertyStatement': <SyntaxKind.CoverPropertyStatement: 107>, 'CoverSequenceStatement': <SyntaxKind.CoverSequenceStatement: 108>, 'CoverageBins': <SyntaxKind.CoverageBins: 109>, 'CoverageBinsArraySize': <SyntaxKind.CoverageBinsArraySize: 110>, 'CoverageIffClause': <SyntaxKind.CoverageIffClause: 111>, 'CoverageOption': <SyntaxKind.CoverageOption: 112>, 'CovergroupDeclaration': <SyntaxKind.CovergroupDeclaration: 113>, 'Coverpoint': <SyntaxKind.Coverpoint: 114>, 'CycleDelay': <SyntaxKind.CycleDelay: 115>, 'DPIExport': <SyntaxKind.DPIExport: 116>, 'DPIImport': <SyntaxKind.DPIImport: 117>, 'DataDeclaration': <SyntaxKind.DataDeclaration: 118>, 'Declarator': <SyntaxKind.Declarator: 119>, 'DefParam': <SyntaxKind.DefParam: 120>, 'DefParamAssignment': <SyntaxKind.DefParamAssignment: 121>, 'DefaultCaseItem': <SyntaxKind.DefaultCaseItem: 122>, 'DefaultClockingReference': <SyntaxKind.DefaultClockingReference: 123>, 'DefaultConfigRule': <SyntaxKind.DefaultConfigRule: 124>, 'DefaultCoverageBinInitializer': <SyntaxKind.DefaultCoverageBinInitializer: 125>, 'DefaultDecayTimeDirective': <SyntaxKind.DefaultDecayTimeDirective: 126>, 'DefaultDisableDeclaration': <SyntaxKind.DefaultDisableDeclaration: 127>, 'DefaultDistItem': <SyntaxKind.DefaultDistItem: 128>, 'DefaultExtendsClauseArg': <SyntaxKind.DefaultExtendsClauseArg: 129>, 'DefaultFunctionPort': <SyntaxKind.DefaultFunctionPort: 130>, 'DefaultNetTypeDirective': <SyntaxKind.DefaultNetTypeDirective: 131>, 'DefaultPatternKeyExpression': <SyntaxKind.DefaultPatternKeyExpression: 132>, 'DefaultPropertyCaseItem': <SyntaxKind.DefaultPropertyCaseItem: 133>, 'DefaultRsCaseItem': <SyntaxKind.DefaultRsCaseItem: 134>, 'DefaultSkewItem': <SyntaxKind.DefaultSkewItem: 135>, 'DefaultTriregStrengthDirective': <SyntaxKind.DefaultTriregStrengthDirective: 136>, 'DeferredAssertion': <SyntaxKind.DeferredAssertion: 137>, 'DefineDirective': <SyntaxKind.DefineDirective: 138>, 'Delay3': <SyntaxKind.Delay3: 139>, 'DelayControl': <SyntaxKind.DelayControl: 140>, 'DelayModeDistributedDirective': <SyntaxKind.DelayModeDistributedDirective: 141>, 'DelayModePathDirective': <SyntaxKind.DelayModePathDirective: 142>, 'DelayModeUnitDirective': <SyntaxKind.DelayModeUnitDirective: 143>, 'DelayModeZeroDirective': <SyntaxKind.DelayModeZeroDirective: 144>, 'DelayedSequenceElement': <SyntaxKind.DelayedSequenceElement: 145>, 'DelayedSequenceExpr': <SyntaxKind.DelayedSequenceExpr: 146>, 'DescendingRangeSelect': <SyntaxKind.DescendingRangeSelect: 147>, 'DisableConstraint': <SyntaxKind.DisableConstraint: 148>, 'DisableForkStatement': <SyntaxKind.DisableForkStatement: 149>, 'DisableIff': <SyntaxKind.DisableIff: 150>, 'DisableStatement': <SyntaxKind.DisableStatement: 151>, 'DistConstraintList': <SyntaxKind.DistConstraintList: 152>, 'DistItem': <SyntaxKind.DistItem: 153>, 'DistWeight': <SyntaxKind.DistWeight: 154>, 'DivideAssignmentExpression': <SyntaxKind.DivideAssignmentExpression: 155>, 'DivideExpression': <SyntaxKind.DivideExpression: 156>, 'DividerClause': <SyntaxKind.DividerClause: 157>, 'DoWhileStatement': <SyntaxKind.DoWhileStatement: 158>, 'DotMemberClause': <SyntaxKind.DotMemberClause: 159>, 'DriveStrength': <SyntaxKind.DriveStrength: 160>, 'EdgeControlSpecifier': <SyntaxKind.EdgeControlSpecifier: 161>, 'EdgeDescriptor': <SyntaxKind.EdgeDescriptor: 162>, 'EdgeSensitivePathSuffix': <SyntaxKind.EdgeSensitivePathSuffix: 163>, 'ElabSystemTask': <SyntaxKind.ElabSystemTask: 164>, 'ElementSelect': <SyntaxKind.ElementSelect: 165>, 'ElementSelectExpression': <SyntaxKind.ElementSelectExpression: 166>, 'ElsIfDirective': <SyntaxKind.ElsIfDirective: 167>, 'ElseClause': <SyntaxKind.ElseClause: 168>, 'ElseConstraintClause': <SyntaxKind.ElseConstraintClause: 169>, 'ElseDirective': <SyntaxKind.ElseDirective: 170>, 'ElsePropertyClause': <SyntaxKind.ElsePropertyClause: 171>, 'EmptyArgument': <SyntaxKind.EmptyArgument: 172>, 'EmptyIdentifierName': <SyntaxKind.EmptyIdentifierName: 173>, 'EmptyMember': <SyntaxKind.EmptyMember: 174>, 'EmptyNonAnsiPort': <SyntaxKind.EmptyNonAnsiPort: 175>, 'EmptyPortConnection': <SyntaxKind.EmptyPortConnection: 176>, 'EmptyQueueExpression': <SyntaxKind.EmptyQueueExpression: 177>, 'EmptyStatement': <SyntaxKind.EmptyStatement: 178>, 'EmptyTimingCheckArg': <SyntaxKind.EmptyTimingCheckArg: 179>, 'EndCellDefineDirective': <SyntaxKind.EndCellDefineDirective: 180>, 'EndIfDirective': <SyntaxKind.EndIfDirective: 181>, 'EndKeywordsDirective': <SyntaxKind.EndKeywordsDirective: 182>, 'EndProtectDirective': <SyntaxKind.EndProtectDirective: 183>, 'EndProtectedDirective': <SyntaxKind.EndProtectedDirective: 184>, 'EnumType': <SyntaxKind.EnumType: 185>, 'EqualityExpression': <SyntaxKind.EqualityExpression: 186>, 'EqualsAssertionArgClause': <SyntaxKind.EqualsAssertionArgClause: 187>, 'EqualsTypeClause': <SyntaxKind.EqualsTypeClause: 188>, 'EqualsValueClause': <SyntaxKind.EqualsValueClause: 189>, 'EventControl': <SyntaxKind.EventControl: 190>, 'EventControlWithExpression': <SyntaxKind.EventControlWithExpression: 191>, 'EventType': <SyntaxKind.EventType: 192>, 'ExpectPropertyStatement': <SyntaxKind.ExpectPropertyStatement: 193>, 'ExplicitAnsiPort': <SyntaxKind.ExplicitAnsiPort: 194>, 'ExplicitNonAnsiPort': <SyntaxKind.ExplicitNonAnsiPort: 195>, 'ExpressionConstraint': <SyntaxKind.ExpressionConstraint: 196>, 'ExpressionCoverageBinInitializer': <SyntaxKind.ExpressionCoverageBinInitializer: 197>, 'ExpressionOrDist': <SyntaxKind.ExpressionOrDist: 198>, 'ExpressionPattern': <SyntaxKind.ExpressionPattern: 199>, 'ExpressionStatement': <SyntaxKind.ExpressionStatement: 200>, 'ExpressionTimingCheckArg': <SyntaxKind.ExpressionTimingCheckArg: 201>, 'ExtendsClause': <SyntaxKind.ExtendsClause: 202>, 'ExternInterfaceMethod': <SyntaxKind.ExternInterfaceMethod: 203>, 'ExternModuleDecl': <SyntaxKind.ExternModuleDecl: 204>, 'ExternUdpDecl': <SyntaxKind.ExternUdpDecl: 205>, 'FilePathSpec': <SyntaxKind.FilePathSpec: 206>, 'FinalBlock': <SyntaxKind.FinalBlock: 207>, 'FirstMatchSequenceExpr': <SyntaxKind.FirstMatchSequenceExpr: 208>, 'FollowedByPropertyExpr': <SyntaxKind.FollowedByPropertyExpr: 209>, 'ForLoopStatement': <SyntaxKind.ForLoopStatement: 210>, 'ForVariableDeclaration': <SyntaxKind.ForVariableDeclaration: 211>, 'ForeachLoopList': <SyntaxKind.ForeachLoopList: 212>, 'ForeachLoopStatement': <SyntaxKind.ForeachLoopStatement: 213>, 'ForeverStatement': <SyntaxKind.ForeverStatement: 214>, 'ForwardTypeRestriction': <SyntaxKind.ForwardTypeRestriction: 215>, 'ForwardTypedefDeclaration': <SyntaxKind.ForwardTypedefDeclaration: 216>, 'FunctionDeclaration': <SyntaxKind.FunctionDeclaration: 217>, 'FunctionPort': <SyntaxKind.FunctionPort: 218>, 'FunctionPortList': <SyntaxKind.FunctionPortList: 219>, 'FunctionPrototype': <SyntaxKind.FunctionPrototype: 220>, 'GenerateBlock': <SyntaxKind.GenerateBlock: 221>, 'GenerateRegion': <SyntaxKind.GenerateRegion: 222>, 'GenvarDeclaration': <SyntaxKind.GenvarDeclaration: 223>, 'GreaterThanEqualExpression': <SyntaxKind.GreaterThanEqualExpression: 224>, 'GreaterThanExpression': <SyntaxKind.GreaterThanExpression: 225>, 'HierarchicalInstance': <SyntaxKind.HierarchicalInstance: 226>, 'HierarchyInstantiation': <SyntaxKind.HierarchyInstantiation: 227>, 'IdWithExprCoverageBinInitializer': <SyntaxKind.IdWithExprCoverageBinInitializer: 228>, 'IdentifierName': <SyntaxKind.IdentifierName: 229>, 'IdentifierSelectName': <SyntaxKind.IdentifierSelectName: 230>, 'IfDefDirective': <SyntaxKind.IfDefDirective: 231>, 'IfGenerate': <SyntaxKind.IfGenerate: 232>, 'IfNDefDirective': <SyntaxKind.IfNDefDirective: 233>, 'IfNonePathDeclaration': <SyntaxKind.IfNonePathDeclaration: 234>, 'IffEventClause': <SyntaxKind.IffEventClause: 235>, 'IffPropertyExpr': <SyntaxKind.IffPropertyExpr: 236>, 'ImmediateAssertStatement': <SyntaxKind.ImmediateAssertStatement: 237>, 'ImmediateAssertionMember': <SyntaxKind.ImmediateAssertionMember: 238>, 'ImmediateAssumeStatement': <SyntaxKind.ImmediateAssumeStatement: 239>, 'ImmediateCoverStatement': <SyntaxKind.ImmediateCoverStatement: 240>, 'ImplementsClause': <SyntaxKind.ImplementsClause: 241>, 'ImplicationConstraint': <SyntaxKind.ImplicationConstraint: 242>, 'ImplicationPropertyExpr': <SyntaxKind.ImplicationPropertyExpr: 243>, 'ImplicitAnsiPort': <SyntaxKind.ImplicitAnsiPort: 244>, 'ImplicitEventControl': <SyntaxKind.ImplicitEventControl: 245>, 'ImplicitNonAnsiPort': <SyntaxKind.ImplicitNonAnsiPort: 246>, 'ImplicitType': <SyntaxKind.ImplicitType: 247>, 'ImpliesPropertyExpr': <SyntaxKind.ImpliesPropertyExpr: 248>, 'IncludeDirective': <SyntaxKind.IncludeDirective: 249>, 'InequalityExpression': <SyntaxKind.InequalityExpression: 250>, 'InitialBlock': <SyntaxKind.InitialBlock: 251>, 'InsideExpression': <SyntaxKind.InsideExpression: 252>, 'InstanceConfigRule': <SyntaxKind.InstanceConfigRule: 253>, 'InstanceName': <SyntaxKind.InstanceName: 254>, 'IntType': <SyntaxKind.IntType: 255>, 'IntegerLiteralExpression': <SyntaxKind.IntegerLiteralExpression: 256>, 'IntegerType': <SyntaxKind.IntegerType: 257>, 'IntegerVectorExpression': <SyntaxKind.IntegerVectorExpression: 258>, 'InterfaceDeclaration': <SyntaxKind.InterfaceDeclaration: 259>, 'InterfaceHeader': <SyntaxKind.InterfaceHeader: 260>, 'InterfacePortHeader': <SyntaxKind.InterfacePortHeader: 261>, 'IntersectClause': <SyntaxKind.IntersectClause: 262>, 'IntersectSequenceExpr': <SyntaxKind.IntersectSequenceExpr: 263>, 'InvocationExpression': <SyntaxKind.InvocationExpression: 264>, 'JumpStatement': <SyntaxKind.JumpStatement: 265>, 'LessThanEqualExpression': <SyntaxKind.LessThanEqualExpression: 266>, 'LessThanExpression': <SyntaxKind.LessThanExpression: 267>, 'LetDeclaration': <SyntaxKind.LetDeclaration: 268>, 'LibraryDeclaration': <SyntaxKind.LibraryDeclaration: 269>, 'LibraryIncDirClause': <SyntaxKind.LibraryIncDirClause: 270>, 'LibraryIncludeStatement': <SyntaxKind.LibraryIncludeStatement: 271>, 'LibraryMap': <SyntaxKind.LibraryMap: 272>, 'LineDirective': <SyntaxKind.LineDirective: 273>, 'LocalScope': <SyntaxKind.LocalScope: 274>, 'LocalVariableDeclaration': <SyntaxKind.LocalVariableDeclaration: 275>, 'LogicType': <SyntaxKind.LogicType: 276>, 'LogicalAndExpression': <SyntaxKind.LogicalAndExpression: 277>, 'LogicalEquivalenceExpression': <SyntaxKind.LogicalEquivalenceExpression: 278>, 'LogicalImplicationExpression': <SyntaxKind.LogicalImplicationExpression: 279>, 'LogicalLeftShiftAssignmentExpression': <SyntaxKind.LogicalLeftShiftAssignmentExpression: 280>, 'LogicalOrExpression': <SyntaxKind.LogicalOrExpression: 281>, 'LogicalRightShiftAssignmentExpression': <SyntaxKind.LogicalRightShiftAssignmentExpression: 282>, 'LogicalShiftLeftExpression': <SyntaxKind.LogicalShiftLeftExpression: 283>, 'LogicalShiftRightExpression': <SyntaxKind.LogicalShiftRightExpression: 284>, 'LongIntType': <SyntaxKind.LongIntType: 285>, 'LoopConstraint': <SyntaxKind.LoopConstraint: 286>, 'LoopGenerate': <SyntaxKind.LoopGenerate: 287>, 'LoopStatement': <SyntaxKind.LoopStatement: 288>, 'MacroActualArgument': <SyntaxKind.MacroActualArgument: 289>, 'MacroActualArgumentList': <SyntaxKind.MacroActualArgumentList: 290>, 'MacroArgumentDefault': <SyntaxKind.MacroArgumentDefault: 291>, 'MacroFormalArgument': <SyntaxKind.MacroFormalArgument: 292>, 'MacroFormalArgumentList': <SyntaxKind.MacroFormalArgumentList: 293>, 'MacroUsage': <SyntaxKind.MacroUsage: 294>, 'MatchesClause': <SyntaxKind.MatchesClause: 295>, 'MemberAccessExpression': <SyntaxKind.MemberAccessExpression: 296>, 'MinTypMaxExpression': <SyntaxKind.MinTypMaxExpression: 297>, 'ModAssignmentExpression': <SyntaxKind.ModAssignmentExpression: 298>, 'ModExpression': <SyntaxKind.ModExpression: 299>, 'ModportClockingPort': <SyntaxKind.ModportClockingPort: 300>, 'ModportDeclaration': <SyntaxKind.ModportDeclaration: 301>, 'ModportExplicitPort': <SyntaxKind.ModportExplicitPort: 302>, 'ModportItem': <SyntaxKind.ModportItem: 303>, 'ModportNamedPort': <SyntaxKind.ModportNamedPort: 304>, 'ModportSimplePortList': <SyntaxKind.ModportSimplePortList: 305>, 'ModportSubroutinePort': <SyntaxKind.ModportSubroutinePort: 306>, 'ModportSubroutinePortList': <SyntaxKind.ModportSubroutinePortList: 307>, 'ModuleDeclaration': <SyntaxKind.ModuleDeclaration: 308>, 'ModuleHeader': <SyntaxKind.ModuleHeader: 309>, 'MultipleConcatenationExpression': <SyntaxKind.MultipleConcatenationExpression: 310>, 'MultiplyAssignmentExpression': <SyntaxKind.MultiplyAssignmentExpression: 311>, 'MultiplyExpression': <SyntaxKind.MultiplyExpression: 312>, 'NameValuePragmaExpression': <SyntaxKind.NameValuePragmaExpression: 313>, 'NamedArgument': <SyntaxKind.NamedArgument: 314>, 'NamedBlockClause': <SyntaxKind.NamedBlockClause: 315>, 'NamedConditionalDirectiveExpression': <SyntaxKind.NamedConditionalDirectiveExpression: 316>, 'NamedLabel': <SyntaxKind.NamedLabel: 317>, 'NamedParamAssignment': <SyntaxKind.NamedParamAssignment: 318>, 'NamedPortConnection': <SyntaxKind.NamedPortConnection: 319>, 'NamedStructurePatternMember': <SyntaxKind.NamedStructurePatternMember: 320>, 'NamedType': <SyntaxKind.NamedType: 321>, 'NetAlias': <SyntaxKind.NetAlias: 322>, 'NetDeclaration': <SyntaxKind.NetDeclaration: 323>, 'NetPortHeader': <SyntaxKind.NetPortHeader: 324>, 'NetTypeDeclaration': <SyntaxKind.NetTypeDeclaration: 325>, 'NewArrayExpression': <SyntaxKind.NewArrayExpression: 326>, 'NewClassExpression': <SyntaxKind.NewClassExpression: 327>, 'NoUnconnectedDriveDirective': <SyntaxKind.NoUnconnectedDriveDirective: 328>, 'NonAnsiPortList': <SyntaxKind.NonAnsiPortList: 329>, 'NonAnsiUdpPortList': <SyntaxKind.NonAnsiUdpPortList: 330>, 'NonblockingAssignmentExpression': <SyntaxKind.NonblockingAssignmentExpression: 331>, 'NonblockingEventTriggerStatement': <SyntaxKind.NonblockingEventTriggerStatement: 332>, 'NullLiteralExpression': <SyntaxKind.NullLiteralExpression: 333>, 'NumberPragmaExpression': <SyntaxKind.NumberPragmaExpression: 334>, 'OneStepDelay': <SyntaxKind.OneStepDelay: 335>, 'OrAssignmentExpression': <SyntaxKind.OrAssignmentExpression: 336>, 'OrPropertyExpr': <SyntaxKind.OrPropertyExpr: 337>, 'OrSequenceExpr': <SyntaxKind.OrSequenceExpr: 338>, 'OrderedArgument': <SyntaxKind.OrderedArgument: 339>, 'OrderedParamAssignment': <SyntaxKind.OrderedParamAssignment: 340>, 'OrderedPortConnection': <SyntaxKind.OrderedPortConnection: 341>, 'OrderedStructurePatternMember': <SyntaxKind.OrderedStructurePatternMember: 342>, 'PackageDeclaration': <SyntaxKind.PackageDeclaration: 343>, 'PackageExportAllDeclaration': <SyntaxKind.PackageExportAllDeclaration: 344>, 'PackageExportDeclaration': <SyntaxKind.PackageExportDeclaration: 345>, 'PackageHeader': <SyntaxKind.PackageHeader: 346>, 'PackageImportDeclaration': <SyntaxKind.PackageImportDeclaration: 347>, 'PackageImportItem': <SyntaxKind.PackageImportItem: 348>, 'ParallelBlockStatement': <SyntaxKind.ParallelBlockStatement: 349>, 'ParameterDeclaration': <SyntaxKind.ParameterDeclaration: 350>, 'ParameterDeclarationStatement': <SyntaxKind.ParameterDeclarationStatement: 351>, 'ParameterPortList': <SyntaxKind.ParameterPortList: 352>, 'ParameterValueAssignment': <SyntaxKind.ParameterValueAssignment: 353>, 'ParenExpressionList': <SyntaxKind.ParenExpressionList: 354>, 'ParenPragmaExpression': <SyntaxKind.ParenPragmaExpression: 355>, 'ParenthesizedBinsSelectExpr': <SyntaxKind.ParenthesizedBinsSelectExpr: 356>, 'ParenthesizedConditionalDirectiveExpression': <SyntaxKind.ParenthesizedConditionalDirectiveExpression: 357>, 'ParenthesizedEventExpression': <SyntaxKind.ParenthesizedEventExpression: 358>, 'ParenthesizedExpression': <SyntaxKind.ParenthesizedExpression: 359>, 'ParenthesizedPattern': <SyntaxKind.ParenthesizedPattern: 360>, 'ParenthesizedPropertyExpr': <SyntaxKind.ParenthesizedPropertyExpr: 361>, 'ParenthesizedSequenceExpr': <SyntaxKind.ParenthesizedSequenceExpr: 362>, 'PathDeclaration': <SyntaxKind.PathDeclaration: 363>, 'PathDescription': <SyntaxKind.PathDescription: 364>, 'PatternCaseItem': <SyntaxKind.PatternCaseItem: 365>, 'PortConcatenation': <SyntaxKind.PortConcatenation: 366>, 'PortDeclaration': <SyntaxKind.PortDeclaration: 367>, 'PortReference': <SyntaxKind.PortReference: 368>, 'PostdecrementExpression': <SyntaxKind.PostdecrementExpression: 369>, 'PostincrementExpression': <SyntaxKind.PostincrementExpression: 370>, 'PowerExpression': <SyntaxKind.PowerExpression: 371>, 'PragmaDirective': <SyntaxKind.PragmaDirective: 372>, 'PrimaryBlockEventExpression': <SyntaxKind.PrimaryBlockEventExpression: 373>, 'PrimitiveInstantiation': <SyntaxKind.PrimitiveInstantiation: 374>, 'ProceduralAssignStatement': <SyntaxKind.ProceduralAssignStatement: 375>, 'ProceduralDeassignStatement': <SyntaxKind.ProceduralDeassignStatement: 376>, 'ProceduralForceStatement': <SyntaxKind.ProceduralForceStatement: 377>, 'ProceduralReleaseStatement': <SyntaxKind.ProceduralReleaseStatement: 378>, 'Production': <SyntaxKind.Production: 379>, 'ProgramDeclaration': <SyntaxKind.ProgramDeclaration: 380>, 'ProgramHeader': <SyntaxKind.ProgramHeader: 381>, 'PropertyDeclaration': <SyntaxKind.PropertyDeclaration: 382>, 'PropertySpec': <SyntaxKind.PropertySpec: 383>, 'PropertyType': <SyntaxKind.PropertyType: 384>, 'ProtectDirective': <SyntaxKind.ProtectDirective: 385>, 'ProtectedDirective': <SyntaxKind.ProtectedDirective: 386>, 'PullStrength': <SyntaxKind.PullStrength: 387>, 'PulseStyleDeclaration': <SyntaxKind.PulseStyleDeclaration: 388>, 'QueueDimensionSpecifier': <SyntaxKind.QueueDimensionSpecifier: 389>, 'RandCaseItem': <SyntaxKind.RandCaseItem: 390>, 'RandCaseStatement': <SyntaxKind.RandCaseStatement: 391>, 'RandJoinClause': <SyntaxKind.RandJoinClause: 392>, 'RandSequenceStatement': <SyntaxKind.RandSequenceStatement: 393>, 'RangeCoverageBinInitializer': <SyntaxKind.RangeCoverageBinInitializer: 394>, 'RangeDimensionSpecifier': <SyntaxKind.RangeDimensionSpecifier: 395>, 'RangeList': <SyntaxKind.RangeList: 396>, 'RealLiteralExpression': <SyntaxKind.RealLiteralExpression: 397>, 'RealTimeType': <SyntaxKind.RealTimeType: 398>, 'RealType': <SyntaxKind.RealType: 399>, 'RegType': <SyntaxKind.RegType: 400>, 'RepeatedEventControl': <SyntaxKind.RepeatedEventControl: 401>, 'ReplicatedAssignmentPattern': <SyntaxKind.ReplicatedAssignmentPattern: 402>, 'ResetAllDirective': <SyntaxKind.ResetAllDirective: 403>, 'RestrictPropertyStatement': <SyntaxKind.RestrictPropertyStatement: 404>, 'ReturnStatement': <SyntaxKind.ReturnStatement: 405>, 'RootScope': <SyntaxKind.RootScope: 406>, 'RsCase': <SyntaxKind.RsCase: 407>, 'RsCodeBlock': <SyntaxKind.RsCodeBlock: 408>, 'RsElseClause': <SyntaxKind.RsElseClause: 409>, 'RsIfElse': <SyntaxKind.RsIfElse: 410>, 'RsProdItem': <SyntaxKind.RsProdItem: 411>, 'RsRepeat': <SyntaxKind.RsRepeat: 412>, 'RsRule': <SyntaxKind.RsRule: 413>, 'RsWeightClause': <SyntaxKind.RsWeightClause: 414>, 'SUntilPropertyExpr': <SyntaxKind.SUntilPropertyExpr: 415>, 'SUntilWithPropertyExpr': <SyntaxKind.SUntilWithPropertyExpr: 416>, 'ScopedName': <SyntaxKind.ScopedName: 417>, 'SequenceDeclaration': <SyntaxKind.SequenceDeclaration: 418>, 'SequenceMatchList': <SyntaxKind.SequenceMatchList: 419>, 'SequenceRepetition': <SyntaxKind.SequenceRepetition: 420>, 'SequenceType': <SyntaxKind.SequenceType: 421>, 'SequentialBlockStatement': <SyntaxKind.SequentialBlockStatement: 422>, 'ShortIntType': <SyntaxKind.ShortIntType: 423>, 'ShortRealType': <SyntaxKind.ShortRealType: 424>, 'SignalEventExpression': <SyntaxKind.SignalEventExpression: 425>, 'SignedCastExpression': <SyntaxKind.SignedCastExpression: 426>, 'SimpleAssignmentPattern': <SyntaxKind.SimpleAssignmentPattern: 427>, 'SimpleBinsSelectExpr': <SyntaxKind.SimpleBinsSelectExpr: 428>, 'SimplePathSuffix': <SyntaxKind.SimplePathSuffix: 429>, 'SimplePragmaExpression': <SyntaxKind.SimplePragmaExpression: 430>, 'SimplePropertyExpr': <SyntaxKind.SimplePropertyExpr: 431>, 'SimpleRangeSelect': <SyntaxKind.SimpleRangeSelect: 432>, 'SimpleSequenceExpr': <SyntaxKind.SimpleSequenceExpr: 433>, 'SolveBeforeConstraint': <SyntaxKind.SolveBeforeConstraint: 434>, 'SpecifyBlock': <SyntaxKind.SpecifyBlock: 435>, 'SpecparamDeclaration': <SyntaxKind.SpecparamDeclaration: 436>, 'SpecparamDeclarator': <SyntaxKind.SpecparamDeclarator: 437>, 'StandardCaseItem': <SyntaxKind.StandardCaseItem: 438>, 'StandardPropertyCaseItem': <SyntaxKind.StandardPropertyCaseItem: 439>, 'StandardRsCaseItem': <SyntaxKind.StandardRsCaseItem: 440>, 'StreamExpression': <SyntaxKind.StreamExpression: 441>, 'StreamExpressionWithRange': <SyntaxKind.StreamExpressionWithRange: 442>, 'StreamingConcatenationExpression': <SyntaxKind.StreamingConcatenationExpression: 443>, 'StringLiteralExpression': <SyntaxKind.StringLiteralExpression: 444>, 'StringType': <SyntaxKind.StringType: 445>, 'StrongWeakPropertyExpr': <SyntaxKind.StrongWeakPropertyExpr: 446>, 'StructType': <SyntaxKind.StructType: 447>, 'StructUnionMember': <SyntaxKind.StructUnionMember: 448>, 'StructurePattern': <SyntaxKind.StructurePattern: 449>, 'StructuredAssignmentPattern': <SyntaxKind.StructuredAssignmentPattern: 450>, 'SubtractAssignmentExpression': <SyntaxKind.SubtractAssignmentExpression: 451>, 'SubtractExpression': <SyntaxKind.SubtractExpression: 452>, 'SuperHandle': <SyntaxKind.SuperHandle: 453>, 'SuperNewDefaultedArgsExpression': <SyntaxKind.SuperNewDefaultedArgsExpression: 454>, 'SystemName': <SyntaxKind.SystemName: 455>, 'SystemTimingCheck': <SyntaxKind.SystemTimingCheck: 456>, 'TaggedPattern': <SyntaxKind.TaggedPattern: 457>, 'TaggedUnionExpression': <SyntaxKind.TaggedUnionExpression: 458>, 'TaskDeclaration': <SyntaxKind.TaskDeclaration: 459>, 'ThisHandle': <SyntaxKind.ThisHandle: 460>, 'ThroughoutSequenceExpr': <SyntaxKind.ThroughoutSequenceExpr: 461>, 'TimeLiteralExpression': <SyntaxKind.TimeLiteralExpression: 462>, 'TimeScaleDirective': <SyntaxKind.TimeScaleDirective: 463>, 'TimeType': <SyntaxKind.TimeType: 464>, 'TimeUnitsDeclaration': <SyntaxKind.TimeUnitsDeclaration: 465>, 'TimingCheckEventArg': <SyntaxKind.TimingCheckEventArg: 466>, 'TimingCheckEventCondition': <SyntaxKind.TimingCheckEventCondition: 467>, 'TimingControlExpression': <SyntaxKind.TimingControlExpression: 468>, 'TimingControlStatement': <SyntaxKind.TimingControlStatement: 469>, 'TransListCoverageBinInitializer': <SyntaxKind.TransListCoverageBinInitializer: 470>, 'TransRange': <SyntaxKind.TransRange: 471>, 'TransRepeatRange': <SyntaxKind.TransRepeatRange: 472>, 'TransSet': <SyntaxKind.TransSet: 473>, 'TypeAssignment': <SyntaxKind.TypeAssignment: 474>, 'TypeParameterDeclaration': <SyntaxKind.TypeParameterDeclaration: 475>, 'TypeReference': <SyntaxKind.TypeReference: 476>, 'TypedefDeclaration': <SyntaxKind.TypedefDeclaration: 477>, 'UdpBody': <SyntaxKind.UdpBody: 478>, 'UdpDeclaration': <SyntaxKind.UdpDeclaration: 479>, 'UdpEdgeField': <SyntaxKind.UdpEdgeField: 480>, 'UdpEntry': <SyntaxKind.UdpEntry: 481>, 'UdpInitialStmt': <SyntaxKind.UdpInitialStmt: 482>, 'UdpInputPortDecl': <SyntaxKind.UdpInputPortDecl: 483>, 'UdpOutputPortDecl': <SyntaxKind.UdpOutputPortDecl: 484>, 'UdpSimpleField': <SyntaxKind.UdpSimpleField: 485>, 'UnaryBinsSelectExpr': <SyntaxKind.UnaryBinsSelectExpr: 486>, 'UnaryBitwiseAndExpression': <SyntaxKind.UnaryBitwiseAndExpression: 487>, 'UnaryBitwiseNandExpression': <SyntaxKind.UnaryBitwiseNandExpression: 488>, 'UnaryBitwiseNorExpression': <SyntaxKind.UnaryBitwiseNorExpression: 489>, 'UnaryBitwiseNotExpression': <SyntaxKind.UnaryBitwiseNotExpression: 490>, 'UnaryBitwiseOrExpression': <SyntaxKind.UnaryBitwiseOrExpression: 491>, 'UnaryBitwiseXnorExpression': <SyntaxKind.UnaryBitwiseXnorExpression: 492>, 'UnaryBitwiseXorExpression': <SyntaxKind.UnaryBitwiseXorExpression: 493>, 'UnaryConditionalDirectiveExpression': <SyntaxKind.UnaryConditionalDirectiveExpression: 494>, 'UnaryLogicalNotExpression': <SyntaxKind.UnaryLogicalNotExpression: 495>, 'UnaryMinusExpression': <SyntaxKind.UnaryMinusExpression: 496>, 'UnaryPlusExpression': <SyntaxKind.UnaryPlusExpression: 497>, 'UnaryPredecrementExpression': <SyntaxKind.UnaryPredecrementExpression: 498>, 'UnaryPreincrementExpression': <SyntaxKind.UnaryPreincrementExpression: 499>, 'UnaryPropertyExpr': <SyntaxKind.UnaryPropertyExpr: 500>, 'UnarySelectPropertyExpr': <SyntaxKind.UnarySelectPropertyExpr: 501>, 'UnbasedUnsizedLiteralExpression': <SyntaxKind.UnbasedUnsizedLiteralExpression: 502>, 'UnconnectedDriveDirective': <SyntaxKind.UnconnectedDriveDirective: 503>, 'UndefDirective': <SyntaxKind.UndefDirective: 504>, 'UndefineAllDirective': <SyntaxKind.UndefineAllDirective: 505>, 'UnionType': <SyntaxKind.UnionType: 506>, 'UniquenessConstraint': <SyntaxKind.UniquenessConstraint: 507>, 'UnitScope': <SyntaxKind.UnitScope: 508>, 'UntilPropertyExpr': <SyntaxKind.UntilPropertyExpr: 509>, 'UntilWithPropertyExpr': <SyntaxKind.UntilWithPropertyExpr: 510>, 'Untyped': <SyntaxKind.Untyped: 511>, 'UserDefinedNetDeclaration': <SyntaxKind.UserDefinedNetDeclaration: 512>, 'ValueRangeExpression': <SyntaxKind.ValueRangeExpression: 513>, 'VariableDimension': <SyntaxKind.VariableDimension: 514>, 'VariablePattern': <SyntaxKind.VariablePattern: 515>, 'VariablePortHeader': <SyntaxKind.VariablePortHeader: 516>, 'VirtualInterfaceType': <SyntaxKind.VirtualInterfaceType: 517>, 'VoidCastedCallStatement': <SyntaxKind.VoidCastedCallStatement: 518>, 'VoidType': <SyntaxKind.VoidType: 519>, 'WaitForkStatement': <SyntaxKind.WaitForkStatement: 520>, 'WaitOrderStatement': <SyntaxKind.WaitOrderStatement: 521>, 'WaitStatement': <SyntaxKind.WaitStatement: 522>, 'WildcardDimensionSpecifier': <SyntaxKind.WildcardDimensionSpecifier: 523>, 'WildcardEqualityExpression': <SyntaxKind.WildcardEqualityExpression: 524>, 'WildcardInequalityExpression': <SyntaxKind.WildcardInequalityExpression: 525>, 'WildcardLiteralExpression': <SyntaxKind.WildcardLiteralExpression: 526>, 'WildcardPattern': <SyntaxKind.WildcardPattern: 527>, 'WildcardPortConnection': <SyntaxKind.WildcardPortConnection: 528>, 'WildcardPortList': <SyntaxKind.WildcardPortList: 529>, 'WildcardUdpPortList': <SyntaxKind.WildcardUdpPortList: 530>, 'WithClause': <SyntaxKind.WithClause: 531>, 'WithFunctionClause': <SyntaxKind.WithFunctionClause: 532>, 'WithFunctionSample': <SyntaxKind.WithFunctionSample: 533>, 'WithinSequenceExpr': <SyntaxKind.WithinSequenceExpr: 534>, 'XorAssignmentExpression': <SyntaxKind.XorAssignmentExpression: 535>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SyntaxNode:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __getitem__(self, arg0: int) -> typing.Any:
        ...
    def __iter__(self) -> typing.Iterator[typing.Any]:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def getFirstToken(self) -> Token:
        ...
    def getLastToken(self) -> Token:
        ...
    def isEquivalentTo(self, other: SyntaxNode) -> bool:
        ...
    def visit(self, f: typing.Any) -> None:
        """
        Visit a pyslang object with a callback f.

        If f ever returns pyslang.VisitAction.Interrupt, the visit is aborted, and no additional nodes are visited. If f returns pyslang.VisitAction.Skip, then no child nodes of the current node are visited, but otherwise the visit continues. Any other return value, including pslang.VisitAction.Advance is ignored, and the walk continues.
        """
    @property
    def kind(self) -> SyntaxKind:
        ...
    @property
    def parent(self) -> SyntaxNode:
        ...
    @property
    def sourceRange(self) -> SourceRange:
        ...
class SyntaxPrinter:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def printFile(tree: SyntaxTree) -> str:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, sourceManager: SourceManager) -> None:
        ...
    def append(self, text: str) -> SyntaxPrinter:
        ...
    @typing.overload
    def print(self, trivia: Trivia) -> SyntaxPrinter:
        ...
    @typing.overload
    def print(self, token: Token) -> SyntaxPrinter:
        ...
    @typing.overload
    def print(self, node: SyntaxNode) -> SyntaxPrinter:
        ...
    @typing.overload
    def print(self, tree: SyntaxTree) -> SyntaxPrinter:
        ...
    def setIncludeComments(self, include: bool) -> SyntaxPrinter:
        ...
    def setIncludeDirectives(self, include: bool) -> SyntaxPrinter:
        ...
    def setIncludeMissing(self, include: bool) -> SyntaxPrinter:
        ...
    def setIncludePreprocessed(self, include: bool) -> SyntaxPrinter:
        ...
    def setIncludeSkipped(self, include: bool) -> SyntaxPrinter:
        ...
    def setIncludeTrivia(self, include: bool) -> SyntaxPrinter:
        ...
    def setSquashNewlines(self, include: bool) -> SyntaxPrinter:
        ...
    def str(self) -> str:
        ...
class SyntaxTree:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def fromBuffer(buffer: SourceBuffer, sourceManager: SourceManager, options: Bag = ..., inheritedMacros: span[...] = []) -> SyntaxTree:
        ...
    @staticmethod
    def fromBuffers(buffers: span[SourceBuffer], sourceManager: SourceManager, options: Bag = ..., inheritedMacros: span[...] = []) -> SyntaxTree:
        ...
    @staticmethod
    @typing.overload
    def fromFile(path: str) -> SyntaxTree:
        ...
    @staticmethod
    @typing.overload
    def fromFile(path: str, sourceManager: SourceManager, options: Bag = ...) -> SyntaxTree:
        ...
    @staticmethod
    def fromFileInMemory(text: str, sourceManager: SourceManager, name: str = 'source', path: str = '', options: Bag = ...) -> SyntaxTree:
        ...
    @staticmethod
    @typing.overload
    def fromFiles(paths: span[str]) -> SyntaxTree:
        ...
    @staticmethod
    @typing.overload
    def fromFiles(paths: span[str], sourceManager: SourceManager, options: Bag = ...) -> SyntaxTree:
        ...
    @staticmethod
    def fromLibraryMapBuffer(buffer: SourceBuffer, sourceManager: SourceManager, options: Bag = ...) -> SyntaxTree:
        ...
    @staticmethod
    def fromLibraryMapFile(path: str, sourceManager: SourceManager, options: Bag = ...) -> SyntaxTree:
        ...
    @staticmethod
    def fromLibraryMapText(text: str, sourceManager: SourceManager, name: str = 'source', path: str = '', options: Bag = ...) -> SyntaxTree:
        ...
    @staticmethod
    @typing.overload
    def fromText(text: str, name: str = 'source', path: str = '') -> SyntaxTree:
        ...
    @staticmethod
    @typing.overload
    def fromText(text: str, sourceManager: SourceManager, name: str = 'source', path: str = '', options: Bag = ..., library: SourceLibrary = None) -> SyntaxTree:
        ...
    @staticmethod
    def getDefaultSourceManager() -> SourceManager:
        ...
    @property
    def diagnostics(self) -> Diagnostics:
        ...
    @property
    def isLibraryUnit(self) -> bool:
        ...
    @property
    def options(self) -> Bag:
        ...
    @property
    def root(self) -> SyntaxNode:
        ...
    @property
    def sourceLibrary(self) -> SourceLibrary:
        ...
    @property
    def sourceManager(self) -> SourceManager:
        ...
class SystemNameSyntax(NameSyntax):
    systemIdentifier: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class SystemSubroutine:
    class WithClauseMode:
        """
        Members:

          None_

          Iterator

          Randomize
        """
        Iterator: typing.ClassVar[SystemSubroutine.WithClauseMode]  # value = <WithClauseMode.Iterator: 1>
        None_: typing.ClassVar[SystemSubroutine.WithClauseMode]  # value = <WithClauseMode.None_: 0>
        Randomize: typing.ClassVar[SystemSubroutine.WithClauseMode]  # value = <WithClauseMode.Randomize: 2>
        __members__: typing.ClassVar[dict[str, SystemSubroutine.WithClauseMode]]  # value = {'None_': <WithClauseMode.None_: 0>, 'Iterator': <WithClauseMode.Iterator: 1>, 'Randomize': <WithClauseMode.Randomize: 2>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    hasOutputArgs: bool
    kind: SubroutineKind
    name: str
    withClauseMode: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def unevaluatedContext(sourceContext: ASTContext) -> ASTContext:
        ...
    def __init__(self, name: str, kind: SubroutineKind) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def allowClockingArgument(self, argIndex: int) -> bool:
        ...
    def allowEmptyArgument(self, argIndex: int) -> bool:
        ...
    def badArg(self, context: ASTContext, arg: ...) -> ...:
        ...
    def bindArgument(self, argIndex: int, context: ASTContext, syntax: ..., previousArgs: span[...]) -> ...:
        ...
    def checkArgCount(self, context: ASTContext, isMethod: bool, args: span[...], callRange: ..., min: int, max: int) -> bool:
        ...
    def checkArguments(self, context: ASTContext, args: span[...], range: ..., iterOrThis: ...) -> ...:
        ...
    def eval(self, context: EvalContext, args: span[...], range: ..., callInfo: ...) -> ...:
        ...
    def kindStr(self) -> str:
        ...
    def noHierarchical(self, context: EvalContext, expr: ...) -> bool:
        ...
    def notConst(self, context: EvalContext, range: ...) -> bool:
        ...
class SystemTimingCheckKind:
    """
    Members:

      Unknown

      Setup

      Hold

      SetupHold

      Recovery

      Removal

      RecRem

      Skew

      TimeSkew

      FullSkew

      Period

      Width

      NoChange
    """
    FullSkew: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.FullSkew: 9>
    Hold: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Hold: 2>
    NoChange: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.NoChange: 12>
    Period: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Period: 10>
    RecRem: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.RecRem: 6>
    Recovery: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Recovery: 4>
    Removal: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Removal: 5>
    Setup: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Setup: 1>
    SetupHold: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.SetupHold: 3>
    Skew: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Skew: 7>
    TimeSkew: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.TimeSkew: 8>
    Unknown: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Unknown: 0>
    Width: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Width: 11>
    __members__: typing.ClassVar[dict[str, SystemTimingCheckKind]]  # value = {'Unknown': <SystemTimingCheckKind.Unknown: 0>, 'Setup': <SystemTimingCheckKind.Setup: 1>, 'Hold': <SystemTimingCheckKind.Hold: 2>, 'SetupHold': <SystemTimingCheckKind.SetupHold: 3>, 'Recovery': <SystemTimingCheckKind.Recovery: 4>, 'Removal': <SystemTimingCheckKind.Removal: 5>, 'RecRem': <SystemTimingCheckKind.RecRem: 6>, 'Skew': <SystemTimingCheckKind.Skew: 7>, 'TimeSkew': <SystemTimingCheckKind.TimeSkew: 8>, 'FullSkew': <SystemTimingCheckKind.FullSkew: 9>, 'Period': <SystemTimingCheckKind.Period: 10>, 'Width': <SystemTimingCheckKind.Width: 11>, 'NoChange': <SystemTimingCheckKind.NoChange: 12>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SystemTimingCheckSymbol(Symbol):
    class Arg:
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        @property
        def condition(self) -> Expression:
            ...
        @property
        def edge(self) -> EdgeKind:
            ...
        @property
        def edgeDescriptors(self) -> span[typing.Annotated[list[str], pybind11_stubgen.typing_ext.FixedSize(2)]]:
            ...
        @property
        def expr(self) -> Expression:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def arguments(self) -> span[...]:
        ...
    @property
    def timingCheckKind(self) -> SystemTimingCheckKind:
        ...
class SystemTimingCheckSyntax(MemberSyntax):
    args: ...
    closeParen: Token
    name: Token
    openParen: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TaggedPattern(Pattern):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def member(self) -> ...:
        ...
    @property
    def valuePattern(self) -> Pattern:
        ...
class TaggedPatternSyntax(PatternSyntax):
    memberName: Token
    pattern: PatternSyntax
    tagged: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TaggedUnionExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def member(self) -> ...:
        ...
    @property
    def valueExpr(self) -> Expression:
        ...
class TaggedUnionExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    member: Token
    tagged: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TempVarSymbol(VariableSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TextDiagnosticClient(DiagnosticClient):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def clear(self) -> None:
        ...
    def getString(self) -> str:
        ...
    def report(self, diag: ReportedDiagnostic) -> None:
        ...
    def showColors(self, show: bool) -> None:
        ...
    def showColumn(self, show: bool) -> None:
        ...
    def showHierarchyInstance(self, show: ...) -> None:
        ...
    def showIncludeStack(self, show: bool) -> None:
        ...
    def showLocation(self, show: bool) -> None:
        ...
    def showMacroExpansion(self, show: bool) -> None:
        ...
    def showOptionName(self, show: bool) -> None:
        ...
    def showSourceLine(self, show: bool) -> None:
        ...
class TimeLiteral(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def value(self) -> float:
        ...
class TimeScale:
    __hash__: typing.ClassVar[None] = None
    base: TimeScaleValue
    precision: TimeScaleValue
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def fromString(str: str) -> TimeScale | None:
        ...
    def __eq__(self, arg0: TimeScale) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, base: TimeScaleValue, precision: TimeScaleValue) -> None:
        ...
    def __ne__(self, arg0: TimeScale) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def apply(self, value: float, unit: TimeUnit, roundToPrecision: bool) -> float:
        ...
class TimeScaleDirectiveSyntax(DirectiveSyntax):
    slash: Token
    timePrecision: Token
    timeUnit: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TimeScaleMagnitude:
    """
    Members:

      One

      Ten

      Hundred
    """
    Hundred: typing.ClassVar[TimeScaleMagnitude]  # value = <TimeScaleMagnitude.Hundred: 100>
    One: typing.ClassVar[TimeScaleMagnitude]  # value = <TimeScaleMagnitude.One: 1>
    Ten: typing.ClassVar[TimeScaleMagnitude]  # value = <TimeScaleMagnitude.Ten: 10>
    __members__: typing.ClassVar[dict[str, TimeScaleMagnitude]]  # value = {'One': <TimeScaleMagnitude.One: 1>, 'Ten': <TimeScaleMagnitude.Ten: 10>, 'Hundred': <TimeScaleMagnitude.Hundred: 100>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TimeScaleValue:
    __hash__: typing.ClassVar[None] = None
    magnitude: TimeScaleMagnitude
    unit: TimeUnit
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def fromLiteral(value: float, unit: TimeUnit) -> TimeScaleValue | None:
        ...
    @staticmethod
    def fromString(str: str) -> TimeScaleValue | None:
        ...
    def __eq__(self, arg0: TimeScaleValue) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, unit: TimeUnit, magnitude: TimeScaleMagnitude) -> None:
        ...
    def __ne__(self, arg0: TimeScaleValue) -> bool:
        ...
    def __repr__(self) -> str:
        ...
class TimeUnit:
    """
    Members:

      Seconds

      Milliseconds

      Microseconds

      Nanoseconds

      Picoseconds

      Femtoseconds
    """
    Femtoseconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Femtoseconds: 5>
    Microseconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Microseconds: 2>
    Milliseconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Milliseconds: 1>
    Nanoseconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Nanoseconds: 3>
    Picoseconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Picoseconds: 4>
    Seconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Seconds: 0>
    __members__: typing.ClassVar[dict[str, TimeUnit]]  # value = {'Seconds': <TimeUnit.Seconds: 0>, 'Milliseconds': <TimeUnit.Milliseconds: 1>, 'Microseconds': <TimeUnit.Microseconds: 2>, 'Nanoseconds': <TimeUnit.Nanoseconds: 3>, 'Picoseconds': <TimeUnit.Picoseconds: 4>, 'Femtoseconds': <TimeUnit.Femtoseconds: 5>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TimeUnitsDeclarationSyntax(MemberSyntax):
    divider: DividerClauseSyntax
    keyword: Token
    semi: Token
    time: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TimedStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def stmt(self) -> Statement:
        ...
    @property
    def timing(self) -> TimingControl:
        ...
class TimingCheckArgSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TimingCheckEventArgSyntax(TimingCheckArgSyntax):
    condition: TimingCheckEventConditionSyntax
    controlSpecifier: EdgeControlSpecifierSyntax
    edge: Token
    terminal: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TimingCheckEventConditionSyntax(SyntaxNode):
    expr: ExpressionSyntax
    tripleAnd: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TimingControl:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __repr__(self) -> str:
        ...
    def visit(self, f: typing.Any) -> None:
        """
        Visit a pyslang object with a callback f.

        If f ever returns pyslang.VisitAction.Interrupt, the visit is aborted, and no additional nodes are visited. If f returns pyslang.VisitAction.Skip, then no child nodes of the current node are visited, but otherwise the visit continues. Any other return value, including pslang.VisitAction.Advance is ignored, and the walk continues.
        """
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> TimingControlKind:
        ...
    @property
    def sourceRange(self) -> ...:
        ...
    @property
    def syntax(self) -> ...:
        ...
class TimingControlExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    timing: TimingControlSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TimingControlKind:
    """
    Members:

      Invalid

      Delay

      SignalEvent

      EventList

      ImplicitEvent

      RepeatedEvent

      Delay3

      OneStepDelay

      CycleDelay

      BlockEventList
    """
    BlockEventList: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.BlockEventList: 9>
    CycleDelay: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.CycleDelay: 8>
    Delay: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.Delay: 1>
    Delay3: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.Delay3: 6>
    EventList: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.EventList: 3>
    ImplicitEvent: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.ImplicitEvent: 4>
    Invalid: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.Invalid: 0>
    OneStepDelay: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.OneStepDelay: 7>
    RepeatedEvent: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.RepeatedEvent: 5>
    SignalEvent: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.SignalEvent: 2>
    __members__: typing.ClassVar[dict[str, TimingControlKind]]  # value = {'Invalid': <TimingControlKind.Invalid: 0>, 'Delay': <TimingControlKind.Delay: 1>, 'SignalEvent': <TimingControlKind.SignalEvent: 2>, 'EventList': <TimingControlKind.EventList: 3>, 'ImplicitEvent': <TimingControlKind.ImplicitEvent: 4>, 'RepeatedEvent': <TimingControlKind.RepeatedEvent: 5>, 'Delay3': <TimingControlKind.Delay3: 6>, 'OneStepDelay': <TimingControlKind.OneStepDelay: 7>, 'CycleDelay': <TimingControlKind.CycleDelay: 8>, 'BlockEventList': <TimingControlKind.BlockEventList: 9>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TimingControlStatementSyntax(StatementSyntax):
    statement: StatementSyntax
    timingControl: TimingControlSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TimingControlSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TimingPathSymbol(Symbol):
    class ConnectionKind:
        """
        Members:

          Full

          Parallel
        """
        Full: typing.ClassVar[TimingPathSymbol.ConnectionKind]  # value = <ConnectionKind.Full: 0>
        Parallel: typing.ClassVar[TimingPathSymbol.ConnectionKind]  # value = <ConnectionKind.Parallel: 1>
        __members__: typing.ClassVar[dict[str, TimingPathSymbol.ConnectionKind]]  # value = {'Full': <ConnectionKind.Full: 0>, 'Parallel': <ConnectionKind.Parallel: 1>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class Polarity:
        """
        Members:

          Unknown

          Positive

          Negative
        """
        Negative: typing.ClassVar[TimingPathSymbol.Polarity]  # value = <Polarity.Negative: 2>
        Positive: typing.ClassVar[TimingPathSymbol.Polarity]  # value = <Polarity.Positive: 1>
        Unknown: typing.ClassVar[TimingPathSymbol.Polarity]  # value = <Polarity.Unknown: 0>
        __members__: typing.ClassVar[dict[str, TimingPathSymbol.Polarity]]  # value = {'Unknown': <Polarity.Unknown: 0>, 'Positive': <Polarity.Positive: 1>, 'Negative': <Polarity.Negative: 2>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def conditionExpr(self) -> Expression:
        ...
    @property
    def connectionKind(self) -> ...:
        ...
    @property
    def delays(self) -> span[Expression]:
        ...
    @property
    def edgeIdentifier(self) -> EdgeKind:
        ...
    @property
    def edgePolarity(self) -> ...:
        ...
    @property
    def edgeSourceExpr(self) -> Expression:
        ...
    @property
    def inputs(self) -> span[Expression]:
        ...
    @property
    def isStateDependent(self) -> bool:
        ...
    @property
    def outputs(self) -> span[Expression]:
        ...
    @property
    def polarity(self) -> ...:
        ...
class Token:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: Token) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, strText: str) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, directive: SyntaxKind) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, bit: logic_t) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, value: SVInt) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, value: float, outOfRange: bool, timeUnit: TimeUnit | None) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, base: LiteralBase, isSigned: bool) -> None:
        ...
    def __ne__(self, arg0: Token) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @property
    def isMissing(self) -> bool:
        ...
    @property
    def isOnSameLine(self) -> bool:
        ...
    @property
    def kind(self) -> TokenKind:
        ...
    @property
    def location(self) -> SourceLocation:
        ...
    @property
    def range(self) -> SourceRange:
        ...
    @property
    def rawText(self) -> str:
        ...
    @property
    def trivia(self) -> span[Trivia]:
        ...
    @property
    def value(self) -> typing.Any:
        ...
    @property
    def valueText(self) -> str:
        ...
class TokenKind:
    """
    Members:

      Unknown

      EndOfFile

      Identifier

      SystemIdentifier

      StringLiteral

      IntegerLiteral

      IntegerBase

      UnbasedUnsizedLiteral

      RealLiteral

      TimeLiteral

      Placeholder

      Apostrophe

      ApostropheOpenBrace

      OpenBrace

      CloseBrace

      OpenBracket

      CloseBracket

      OpenParenthesis

      CloseParenthesis

      Semicolon

      Colon

      ColonEquals

      ColonSlash

      DoubleColon

      Comma

      Dot

      Slash

      Star

      DoubleStar

      StarArrow

      Plus

      DoublePlus

      PlusColon

      PlusDivMinus

      PlusModMinus

      Minus

      DoubleMinus

      MinusColon

      MinusArrow

      MinusDoubleArrow

      Tilde

      TildeAnd

      TildeOr

      TildeXor

      Dollar

      Question

      Hash

      DoubleHash

      HashMinusHash

      HashEqualsHash

      Xor

      XorTilde

      Equals

      DoubleEquals

      DoubleEqualsQuestion

      TripleEquals

      EqualsArrow

      PlusEqual

      MinusEqual

      SlashEqual

      StarEqual

      AndEqual

      OrEqual

      PercentEqual

      XorEqual

      LeftShiftEqual

      TripleLeftShiftEqual

      RightShiftEqual

      TripleRightShiftEqual

      LeftShift

      RightShift

      TripleLeftShift

      TripleRightShift

      Exclamation

      ExclamationEquals

      ExclamationEqualsQuestion

      ExclamationDoubleEquals

      Percent

      LessThan

      LessThanEquals

      LessThanMinusArrow

      GreaterThan

      GreaterThanEquals

      Or

      DoubleOr

      OrMinusArrow

      OrEqualsArrow

      At

      DoubleAt

      And

      DoubleAnd

      TripleAnd

      OneStep

      AcceptOnKeyword

      AliasKeyword

      AlwaysKeyword

      AlwaysCombKeyword

      AlwaysFFKeyword

      AlwaysLatchKeyword

      AndKeyword

      AssertKeyword

      AssignKeyword

      AssumeKeyword

      AutomaticKeyword

      BeforeKeyword

      BeginKeyword

      BindKeyword

      BinsKeyword

      BinsOfKeyword

      BitKeyword

      BreakKeyword

      BufKeyword

      BufIf0Keyword

      BufIf1Keyword

      ByteKeyword

      CaseKeyword

      CaseXKeyword

      CaseZKeyword

      CellKeyword

      CHandleKeyword

      CheckerKeyword

      ClassKeyword

      ClockingKeyword

      CmosKeyword

      ConfigKeyword

      ConstKeyword

      ConstraintKeyword

      ContextKeyword

      ContinueKeyword

      CoverKeyword

      CoverGroupKeyword

      CoverPointKeyword

      CrossKeyword

      DeassignKeyword

      DefaultKeyword

      DefParamKeyword

      DesignKeyword

      DisableKeyword

      DistKeyword

      DoKeyword

      EdgeKeyword

      ElseKeyword

      EndKeyword

      EndCaseKeyword

      EndCheckerKeyword

      EndClassKeyword

      EndClockingKeyword

      EndConfigKeyword

      EndFunctionKeyword

      EndGenerateKeyword

      EndGroupKeyword

      EndInterfaceKeyword

      EndModuleKeyword

      EndPackageKeyword

      EndPrimitiveKeyword

      EndProgramKeyword

      EndPropertyKeyword

      EndSpecifyKeyword

      EndSequenceKeyword

      EndTableKeyword

      EndTaskKeyword

      EnumKeyword

      EventKeyword

      EventuallyKeyword

      ExpectKeyword

      ExportKeyword

      ExtendsKeyword

      ExternKeyword

      FinalKeyword

      FirstMatchKeyword

      ForKeyword

      ForceKeyword

      ForeachKeyword

      ForeverKeyword

      ForkKeyword

      ForkJoinKeyword

      FunctionKeyword

      GenerateKeyword

      GenVarKeyword

      GlobalKeyword

      HighZ0Keyword

      HighZ1Keyword

      IfKeyword

      IffKeyword

      IfNoneKeyword

      IgnoreBinsKeyword

      IllegalBinsKeyword

      ImplementsKeyword

      ImpliesKeyword

      ImportKeyword

      IncDirKeyword

      IncludeKeyword

      InitialKeyword

      InOutKeyword

      InputKeyword

      InsideKeyword

      InstanceKeyword

      IntKeyword

      IntegerKeyword

      InterconnectKeyword

      InterfaceKeyword

      IntersectKeyword

      JoinKeyword

      JoinAnyKeyword

      JoinNoneKeyword

      LargeKeyword

      LetKeyword

      LibListKeyword

      LibraryKeyword

      LocalKeyword

      LocalParamKeyword

      LogicKeyword

      LongIntKeyword

      MacromoduleKeyword

      MatchesKeyword

      MediumKeyword

      ModPortKeyword

      ModuleKeyword

      NandKeyword

      NegEdgeKeyword

      NetTypeKeyword

      NewKeyword

      NextTimeKeyword

      NmosKeyword

      NorKeyword

      NoShowCancelledKeyword

      NotKeyword

      NotIf0Keyword

      NotIf1Keyword

      NullKeyword

      OrKeyword

      OutputKeyword

      PackageKeyword

      PackedKeyword

      ParameterKeyword

      PmosKeyword

      PosEdgeKeyword

      PrimitiveKeyword

      PriorityKeyword

      ProgramKeyword

      PropertyKeyword

      ProtectedKeyword

      Pull0Keyword

      Pull1Keyword

      PullDownKeyword

      PullUpKeyword

      PulseStyleOnDetectKeyword

      PulseStyleOnEventKeyword

      PureKeyword

      RandKeyword

      RandCKeyword

      RandCaseKeyword

      RandSequenceKeyword

      RcmosKeyword

      RealKeyword

      RealTimeKeyword

      RefKeyword

      RegKeyword

      RejectOnKeyword

      ReleaseKeyword

      RepeatKeyword

      RestrictKeyword

      ReturnKeyword

      RnmosKeyword

      RpmosKeyword

      RtranKeyword

      RtranIf0Keyword

      RtranIf1Keyword

      SAlwaysKeyword

      SEventuallyKeyword

      SNextTimeKeyword

      SUntilKeyword

      SUntilWithKeyword

      ScalaredKeyword

      SequenceKeyword

      ShortIntKeyword

      ShortRealKeyword

      ShowCancelledKeyword

      SignedKeyword

      SmallKeyword

      SoftKeyword

      SolveKeyword

      SpecifyKeyword

      SpecParamKeyword

      StaticKeyword

      StringKeyword

      StrongKeyword

      Strong0Keyword

      Strong1Keyword

      StructKeyword

      SuperKeyword

      Supply0Keyword

      Supply1Keyword

      SyncAcceptOnKeyword

      SyncRejectOnKeyword

      TableKeyword

      TaggedKeyword

      TaskKeyword

      ThisKeyword

      ThroughoutKeyword

      TimeKeyword

      TimePrecisionKeyword

      TimeUnitKeyword

      TranKeyword

      TranIf0Keyword

      TranIf1Keyword

      TriKeyword

      Tri0Keyword

      Tri1Keyword

      TriAndKeyword

      TriOrKeyword

      TriRegKeyword

      TypeKeyword

      TypedefKeyword

      UnionKeyword

      UniqueKeyword

      Unique0Keyword

      UnsignedKeyword

      UntilKeyword

      UntilWithKeyword

      UntypedKeyword

      UseKeyword

      UWireKeyword

      VarKeyword

      VectoredKeyword

      VirtualKeyword

      VoidKeyword

      WaitKeyword

      WaitOrderKeyword

      WAndKeyword

      WeakKeyword

      Weak0Keyword

      Weak1Keyword

      WhileKeyword

      WildcardKeyword

      WireKeyword

      WithKeyword

      WithinKeyword

      WOrKeyword

      XnorKeyword

      XorKeyword

      UnitSystemName

      RootSystemName

      Directive

      IncludeFileName

      MacroUsage

      MacroQuote

      MacroTripleQuote

      MacroEscapedQuote

      MacroPaste

      EmptyMacroArgument

      LineContinuation
    """
    AcceptOnKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AcceptOnKeyword: 93>
    AliasKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AliasKeyword: 94>
    AlwaysCombKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AlwaysCombKeyword: 96>
    AlwaysFFKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AlwaysFFKeyword: 97>
    AlwaysKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AlwaysKeyword: 95>
    AlwaysLatchKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AlwaysLatchKeyword: 98>
    And: typing.ClassVar[TokenKind]  # value = <TokenKind.And: 89>
    AndEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.AndEqual: 61>
    AndKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AndKeyword: 99>
    Apostrophe: typing.ClassVar[TokenKind]  # value = <TokenKind.Apostrophe: 11>
    ApostropheOpenBrace: typing.ClassVar[TokenKind]  # value = <TokenKind.ApostropheOpenBrace: 12>
    AssertKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AssertKeyword: 100>
    AssignKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AssignKeyword: 101>
    AssumeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AssumeKeyword: 102>
    At: typing.ClassVar[TokenKind]  # value = <TokenKind.At: 87>
    AutomaticKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AutomaticKeyword: 103>
    BeforeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BeforeKeyword: 104>
    BeginKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BeginKeyword: 105>
    BindKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BindKeyword: 106>
    BinsKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BinsKeyword: 107>
    BinsOfKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BinsOfKeyword: 108>
    BitKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BitKeyword: 109>
    BreakKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BreakKeyword: 110>
    BufIf0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BufIf0Keyword: 112>
    BufIf1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BufIf1Keyword: 113>
    BufKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BufKeyword: 111>
    ByteKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ByteKeyword: 114>
    CHandleKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CHandleKeyword: 119>
    CaseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CaseKeyword: 115>
    CaseXKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CaseXKeyword: 116>
    CaseZKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CaseZKeyword: 117>
    CellKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CellKeyword: 118>
    CheckerKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CheckerKeyword: 120>
    ClassKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ClassKeyword: 121>
    ClockingKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ClockingKeyword: 122>
    CloseBrace: typing.ClassVar[TokenKind]  # value = <TokenKind.CloseBrace: 14>
    CloseBracket: typing.ClassVar[TokenKind]  # value = <TokenKind.CloseBracket: 16>
    CloseParenthesis: typing.ClassVar[TokenKind]  # value = <TokenKind.CloseParenthesis: 18>
    CmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CmosKeyword: 123>
    Colon: typing.ClassVar[TokenKind]  # value = <TokenKind.Colon: 20>
    ColonEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.ColonEquals: 21>
    ColonSlash: typing.ClassVar[TokenKind]  # value = <TokenKind.ColonSlash: 22>
    Comma: typing.ClassVar[TokenKind]  # value = <TokenKind.Comma: 24>
    ConfigKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ConfigKeyword: 124>
    ConstKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ConstKeyword: 125>
    ConstraintKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ConstraintKeyword: 126>
    ContextKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ContextKeyword: 127>
    ContinueKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ContinueKeyword: 128>
    CoverGroupKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CoverGroupKeyword: 130>
    CoverKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CoverKeyword: 129>
    CoverPointKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CoverPointKeyword: 131>
    CrossKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CrossKeyword: 132>
    DeassignKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DeassignKeyword: 133>
    DefParamKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DefParamKeyword: 135>
    DefaultKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DefaultKeyword: 134>
    DesignKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DesignKeyword: 136>
    Directive: typing.ClassVar[TokenKind]  # value = <TokenKind.Directive: 343>
    DisableKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DisableKeyword: 137>
    DistKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DistKeyword: 138>
    DoKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DoKeyword: 139>
    Dollar: typing.ClassVar[TokenKind]  # value = <TokenKind.Dollar: 44>
    Dot: typing.ClassVar[TokenKind]  # value = <TokenKind.Dot: 25>
    DoubleAnd: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleAnd: 90>
    DoubleAt: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleAt: 88>
    DoubleColon: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleColon: 23>
    DoubleEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleEquals: 53>
    DoubleEqualsQuestion: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleEqualsQuestion: 54>
    DoubleHash: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleHash: 47>
    DoubleMinus: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleMinus: 36>
    DoubleOr: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleOr: 84>
    DoublePlus: typing.ClassVar[TokenKind]  # value = <TokenKind.DoublePlus: 31>
    DoubleStar: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleStar: 28>
    EdgeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EdgeKeyword: 140>
    ElseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ElseKeyword: 141>
    EmptyMacroArgument: typing.ClassVar[TokenKind]  # value = <TokenKind.EmptyMacroArgument: 350>
    EndCaseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndCaseKeyword: 143>
    EndCheckerKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndCheckerKeyword: 144>
    EndClassKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndClassKeyword: 145>
    EndClockingKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndClockingKeyword: 146>
    EndConfigKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndConfigKeyword: 147>
    EndFunctionKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndFunctionKeyword: 148>
    EndGenerateKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndGenerateKeyword: 149>
    EndGroupKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndGroupKeyword: 150>
    EndInterfaceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndInterfaceKeyword: 151>
    EndKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndKeyword: 142>
    EndModuleKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndModuleKeyword: 152>
    EndOfFile: typing.ClassVar[TokenKind]  # value = <TokenKind.EndOfFile: 1>
    EndPackageKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndPackageKeyword: 153>
    EndPrimitiveKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndPrimitiveKeyword: 154>
    EndProgramKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndProgramKeyword: 155>
    EndPropertyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndPropertyKeyword: 156>
    EndSequenceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndSequenceKeyword: 158>
    EndSpecifyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndSpecifyKeyword: 157>
    EndTableKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndTableKeyword: 159>
    EndTaskKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndTaskKeyword: 160>
    EnumKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EnumKeyword: 161>
    Equals: typing.ClassVar[TokenKind]  # value = <TokenKind.Equals: 52>
    EqualsArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.EqualsArrow: 56>
    EventKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EventKeyword: 162>
    EventuallyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EventuallyKeyword: 163>
    Exclamation: typing.ClassVar[TokenKind]  # value = <TokenKind.Exclamation: 73>
    ExclamationDoubleEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.ExclamationDoubleEquals: 76>
    ExclamationEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.ExclamationEquals: 74>
    ExclamationEqualsQuestion: typing.ClassVar[TokenKind]  # value = <TokenKind.ExclamationEqualsQuestion: 75>
    ExpectKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ExpectKeyword: 164>
    ExportKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ExportKeyword: 165>
    ExtendsKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ExtendsKeyword: 166>
    ExternKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ExternKeyword: 167>
    FinalKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.FinalKeyword: 168>
    FirstMatchKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.FirstMatchKeyword: 169>
    ForKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForKeyword: 170>
    ForceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForceKeyword: 171>
    ForeachKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForeachKeyword: 172>
    ForeverKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForeverKeyword: 173>
    ForkJoinKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForkJoinKeyword: 175>
    ForkKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForkKeyword: 174>
    FunctionKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.FunctionKeyword: 176>
    GenVarKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.GenVarKeyword: 178>
    GenerateKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.GenerateKeyword: 177>
    GlobalKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.GlobalKeyword: 179>
    GreaterThan: typing.ClassVar[TokenKind]  # value = <TokenKind.GreaterThan: 81>
    GreaterThanEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.GreaterThanEquals: 82>
    Hash: typing.ClassVar[TokenKind]  # value = <TokenKind.Hash: 46>
    HashEqualsHash: typing.ClassVar[TokenKind]  # value = <TokenKind.HashEqualsHash: 49>
    HashMinusHash: typing.ClassVar[TokenKind]  # value = <TokenKind.HashMinusHash: 48>
    HighZ0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.HighZ0Keyword: 180>
    HighZ1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.HighZ1Keyword: 181>
    Identifier: typing.ClassVar[TokenKind]  # value = <TokenKind.Identifier: 2>
    IfKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IfKeyword: 182>
    IfNoneKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IfNoneKeyword: 184>
    IffKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IffKeyword: 183>
    IgnoreBinsKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IgnoreBinsKeyword: 185>
    IllegalBinsKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IllegalBinsKeyword: 186>
    ImplementsKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ImplementsKeyword: 187>
    ImpliesKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ImpliesKeyword: 188>
    ImportKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ImportKeyword: 189>
    InOutKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InOutKeyword: 193>
    IncDirKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IncDirKeyword: 190>
    IncludeFileName: typing.ClassVar[TokenKind]  # value = <TokenKind.IncludeFileName: 344>
    IncludeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IncludeKeyword: 191>
    InitialKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InitialKeyword: 192>
    InputKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InputKeyword: 194>
    InsideKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InsideKeyword: 195>
    InstanceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InstanceKeyword: 196>
    IntKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IntKeyword: 197>
    IntegerBase: typing.ClassVar[TokenKind]  # value = <TokenKind.IntegerBase: 6>
    IntegerKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IntegerKeyword: 198>
    IntegerLiteral: typing.ClassVar[TokenKind]  # value = <TokenKind.IntegerLiteral: 5>
    InterconnectKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InterconnectKeyword: 199>
    InterfaceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InterfaceKeyword: 200>
    IntersectKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IntersectKeyword: 201>
    JoinAnyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.JoinAnyKeyword: 203>
    JoinKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.JoinKeyword: 202>
    JoinNoneKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.JoinNoneKeyword: 204>
    LargeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LargeKeyword: 205>
    LeftShift: typing.ClassVar[TokenKind]  # value = <TokenKind.LeftShift: 69>
    LeftShiftEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.LeftShiftEqual: 65>
    LessThan: typing.ClassVar[TokenKind]  # value = <TokenKind.LessThan: 78>
    LessThanEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.LessThanEquals: 79>
    LessThanMinusArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.LessThanMinusArrow: 80>
    LetKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LetKeyword: 206>
    LibListKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LibListKeyword: 207>
    LibraryKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LibraryKeyword: 208>
    LineContinuation: typing.ClassVar[TokenKind]  # value = <TokenKind.LineContinuation: 351>
    LocalKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LocalKeyword: 209>
    LocalParamKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LocalParamKeyword: 210>
    LogicKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LogicKeyword: 211>
    LongIntKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LongIntKeyword: 212>
    MacroEscapedQuote: typing.ClassVar[TokenKind]  # value = <TokenKind.MacroEscapedQuote: 348>
    MacroPaste: typing.ClassVar[TokenKind]  # value = <TokenKind.MacroPaste: 349>
    MacroQuote: typing.ClassVar[TokenKind]  # value = <TokenKind.MacroQuote: 346>
    MacroTripleQuote: typing.ClassVar[TokenKind]  # value = <TokenKind.MacroTripleQuote: 347>
    MacroUsage: typing.ClassVar[TokenKind]  # value = <TokenKind.MacroUsage: 345>
    MacromoduleKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.MacromoduleKeyword: 213>
    MatchesKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.MatchesKeyword: 214>
    MediumKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.MediumKeyword: 215>
    Minus: typing.ClassVar[TokenKind]  # value = <TokenKind.Minus: 35>
    MinusArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.MinusArrow: 38>
    MinusColon: typing.ClassVar[TokenKind]  # value = <TokenKind.MinusColon: 37>
    MinusDoubleArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.MinusDoubleArrow: 39>
    MinusEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.MinusEqual: 58>
    ModPortKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ModPortKeyword: 216>
    ModuleKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ModuleKeyword: 217>
    NandKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NandKeyword: 218>
    NegEdgeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NegEdgeKeyword: 219>
    NetTypeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NetTypeKeyword: 220>
    NewKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NewKeyword: 221>
    NextTimeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NextTimeKeyword: 222>
    NmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NmosKeyword: 223>
    NoShowCancelledKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NoShowCancelledKeyword: 225>
    NorKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NorKeyword: 224>
    NotIf0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NotIf0Keyword: 227>
    NotIf1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NotIf1Keyword: 228>
    NotKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NotKeyword: 226>
    NullKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NullKeyword: 229>
    OneStep: typing.ClassVar[TokenKind]  # value = <TokenKind.OneStep: 92>
    OpenBrace: typing.ClassVar[TokenKind]  # value = <TokenKind.OpenBrace: 13>
    OpenBracket: typing.ClassVar[TokenKind]  # value = <TokenKind.OpenBracket: 15>
    OpenParenthesis: typing.ClassVar[TokenKind]  # value = <TokenKind.OpenParenthesis: 17>
    Or: typing.ClassVar[TokenKind]  # value = <TokenKind.Or: 83>
    OrEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.OrEqual: 62>
    OrEqualsArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.OrEqualsArrow: 86>
    OrKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.OrKeyword: 230>
    OrMinusArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.OrMinusArrow: 85>
    OutputKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.OutputKeyword: 231>
    PackageKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PackageKeyword: 232>
    PackedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PackedKeyword: 233>
    ParameterKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ParameterKeyword: 234>
    Percent: typing.ClassVar[TokenKind]  # value = <TokenKind.Percent: 77>
    PercentEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.PercentEqual: 63>
    Placeholder: typing.ClassVar[TokenKind]  # value = <TokenKind.Placeholder: 10>
    Plus: typing.ClassVar[TokenKind]  # value = <TokenKind.Plus: 30>
    PlusColon: typing.ClassVar[TokenKind]  # value = <TokenKind.PlusColon: 32>
    PlusDivMinus: typing.ClassVar[TokenKind]  # value = <TokenKind.PlusDivMinus: 33>
    PlusEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.PlusEqual: 57>
    PlusModMinus: typing.ClassVar[TokenKind]  # value = <TokenKind.PlusModMinus: 34>
    PmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PmosKeyword: 235>
    PosEdgeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PosEdgeKeyword: 236>
    PrimitiveKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PrimitiveKeyword: 237>
    PriorityKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PriorityKeyword: 238>
    ProgramKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ProgramKeyword: 239>
    PropertyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PropertyKeyword: 240>
    ProtectedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ProtectedKeyword: 241>
    Pull0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Pull0Keyword: 242>
    Pull1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Pull1Keyword: 243>
    PullDownKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PullDownKeyword: 244>
    PullUpKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PullUpKeyword: 245>
    PulseStyleOnDetectKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PulseStyleOnDetectKeyword: 246>
    PulseStyleOnEventKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PulseStyleOnEventKeyword: 247>
    PureKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PureKeyword: 248>
    Question: typing.ClassVar[TokenKind]  # value = <TokenKind.Question: 45>
    RandCKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RandCKeyword: 250>
    RandCaseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RandCaseKeyword: 251>
    RandKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RandKeyword: 249>
    RandSequenceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RandSequenceKeyword: 252>
    RcmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RcmosKeyword: 253>
    RealKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RealKeyword: 254>
    RealLiteral: typing.ClassVar[TokenKind]  # value = <TokenKind.RealLiteral: 8>
    RealTimeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RealTimeKeyword: 255>
    RefKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RefKeyword: 256>
    RegKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RegKeyword: 257>
    RejectOnKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RejectOnKeyword: 258>
    ReleaseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ReleaseKeyword: 259>
    RepeatKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RepeatKeyword: 260>
    RestrictKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RestrictKeyword: 261>
    ReturnKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ReturnKeyword: 262>
    RightShift: typing.ClassVar[TokenKind]  # value = <TokenKind.RightShift: 70>
    RightShiftEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.RightShiftEqual: 67>
    RnmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RnmosKeyword: 263>
    RootSystemName: typing.ClassVar[TokenKind]  # value = <TokenKind.RootSystemName: 342>
    RpmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RpmosKeyword: 264>
    RtranIf0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RtranIf0Keyword: 266>
    RtranIf1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RtranIf1Keyword: 267>
    RtranKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RtranKeyword: 265>
    SAlwaysKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SAlwaysKeyword: 268>
    SEventuallyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SEventuallyKeyword: 269>
    SNextTimeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SNextTimeKeyword: 270>
    SUntilKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SUntilKeyword: 271>
    SUntilWithKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SUntilWithKeyword: 272>
    ScalaredKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ScalaredKeyword: 273>
    Semicolon: typing.ClassVar[TokenKind]  # value = <TokenKind.Semicolon: 19>
    SequenceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SequenceKeyword: 274>
    ShortIntKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ShortIntKeyword: 275>
    ShortRealKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ShortRealKeyword: 276>
    ShowCancelledKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ShowCancelledKeyword: 277>
    SignedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SignedKeyword: 278>
    Slash: typing.ClassVar[TokenKind]  # value = <TokenKind.Slash: 26>
    SlashEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.SlashEqual: 59>
    SmallKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SmallKeyword: 279>
    SoftKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SoftKeyword: 280>
    SolveKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SolveKeyword: 281>
    SpecParamKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SpecParamKeyword: 283>
    SpecifyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SpecifyKeyword: 282>
    Star: typing.ClassVar[TokenKind]  # value = <TokenKind.Star: 27>
    StarArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.StarArrow: 29>
    StarEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.StarEqual: 60>
    StaticKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.StaticKeyword: 284>
    StringKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.StringKeyword: 285>
    StringLiteral: typing.ClassVar[TokenKind]  # value = <TokenKind.StringLiteral: 4>
    Strong0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Strong0Keyword: 287>
    Strong1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Strong1Keyword: 288>
    StrongKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.StrongKeyword: 286>
    StructKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.StructKeyword: 289>
    SuperKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SuperKeyword: 290>
    Supply0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Supply0Keyword: 291>
    Supply1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Supply1Keyword: 292>
    SyncAcceptOnKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SyncAcceptOnKeyword: 293>
    SyncRejectOnKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SyncRejectOnKeyword: 294>
    SystemIdentifier: typing.ClassVar[TokenKind]  # value = <TokenKind.SystemIdentifier: 3>
    TableKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TableKeyword: 295>
    TaggedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TaggedKeyword: 296>
    TaskKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TaskKeyword: 297>
    ThisKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ThisKeyword: 298>
    ThroughoutKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ThroughoutKeyword: 299>
    Tilde: typing.ClassVar[TokenKind]  # value = <TokenKind.Tilde: 40>
    TildeAnd: typing.ClassVar[TokenKind]  # value = <TokenKind.TildeAnd: 41>
    TildeOr: typing.ClassVar[TokenKind]  # value = <TokenKind.TildeOr: 42>
    TildeXor: typing.ClassVar[TokenKind]  # value = <TokenKind.TildeXor: 43>
    TimeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TimeKeyword: 300>
    TimeLiteral: typing.ClassVar[TokenKind]  # value = <TokenKind.TimeLiteral: 9>
    TimePrecisionKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TimePrecisionKeyword: 301>
    TimeUnitKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TimeUnitKeyword: 302>
    TranIf0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TranIf0Keyword: 304>
    TranIf1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TranIf1Keyword: 305>
    TranKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TranKeyword: 303>
    Tri0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Tri0Keyword: 307>
    Tri1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Tri1Keyword: 308>
    TriAndKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TriAndKeyword: 309>
    TriKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TriKeyword: 306>
    TriOrKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TriOrKeyword: 310>
    TriRegKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TriRegKeyword: 311>
    TripleAnd: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleAnd: 91>
    TripleEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleEquals: 55>
    TripleLeftShift: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleLeftShift: 71>
    TripleLeftShiftEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleLeftShiftEqual: 66>
    TripleRightShift: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleRightShift: 72>
    TripleRightShiftEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleRightShiftEqual: 68>
    TypeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TypeKeyword: 312>
    TypedefKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TypedefKeyword: 313>
    UWireKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UWireKeyword: 322>
    UnbasedUnsizedLiteral: typing.ClassVar[TokenKind]  # value = <TokenKind.UnbasedUnsizedLiteral: 7>
    UnionKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UnionKeyword: 314>
    Unique0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Unique0Keyword: 316>
    UniqueKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UniqueKeyword: 315>
    UnitSystemName: typing.ClassVar[TokenKind]  # value = <TokenKind.UnitSystemName: 341>
    Unknown: typing.ClassVar[TokenKind]  # value = <TokenKind.Unknown: 0>
    UnsignedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UnsignedKeyword: 317>
    UntilKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UntilKeyword: 318>
    UntilWithKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UntilWithKeyword: 319>
    UntypedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UntypedKeyword: 320>
    UseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UseKeyword: 321>
    VarKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.VarKeyword: 323>
    VectoredKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.VectoredKeyword: 324>
    VirtualKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.VirtualKeyword: 325>
    VoidKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.VoidKeyword: 326>
    WAndKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WAndKeyword: 329>
    WOrKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WOrKeyword: 338>
    WaitKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WaitKeyword: 327>
    WaitOrderKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WaitOrderKeyword: 328>
    Weak0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Weak0Keyword: 331>
    Weak1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Weak1Keyword: 332>
    WeakKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WeakKeyword: 330>
    WhileKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WhileKeyword: 333>
    WildcardKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WildcardKeyword: 334>
    WireKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WireKeyword: 335>
    WithKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WithKeyword: 336>
    WithinKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WithinKeyword: 337>
    XnorKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.XnorKeyword: 339>
    Xor: typing.ClassVar[TokenKind]  # value = <TokenKind.Xor: 50>
    XorEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.XorEqual: 64>
    XorKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.XorKeyword: 340>
    XorTilde: typing.ClassVar[TokenKind]  # value = <TokenKind.XorTilde: 51>
    __members__: typing.ClassVar[dict[str, TokenKind]]  # value = {'Unknown': <TokenKind.Unknown: 0>, 'EndOfFile': <TokenKind.EndOfFile: 1>, 'Identifier': <TokenKind.Identifier: 2>, 'SystemIdentifier': <TokenKind.SystemIdentifier: 3>, 'StringLiteral': <TokenKind.StringLiteral: 4>, 'IntegerLiteral': <TokenKind.IntegerLiteral: 5>, 'IntegerBase': <TokenKind.IntegerBase: 6>, 'UnbasedUnsizedLiteral': <TokenKind.UnbasedUnsizedLiteral: 7>, 'RealLiteral': <TokenKind.RealLiteral: 8>, 'TimeLiteral': <TokenKind.TimeLiteral: 9>, 'Placeholder': <TokenKind.Placeholder: 10>, 'Apostrophe': <TokenKind.Apostrophe: 11>, 'ApostropheOpenBrace': <TokenKind.ApostropheOpenBrace: 12>, 'OpenBrace': <TokenKind.OpenBrace: 13>, 'CloseBrace': <TokenKind.CloseBrace: 14>, 'OpenBracket': <TokenKind.OpenBracket: 15>, 'CloseBracket': <TokenKind.CloseBracket: 16>, 'OpenParenthesis': <TokenKind.OpenParenthesis: 17>, 'CloseParenthesis': <TokenKind.CloseParenthesis: 18>, 'Semicolon': <TokenKind.Semicolon: 19>, 'Colon': <TokenKind.Colon: 20>, 'ColonEquals': <TokenKind.ColonEquals: 21>, 'ColonSlash': <TokenKind.ColonSlash: 22>, 'DoubleColon': <TokenKind.DoubleColon: 23>, 'Comma': <TokenKind.Comma: 24>, 'Dot': <TokenKind.Dot: 25>, 'Slash': <TokenKind.Slash: 26>, 'Star': <TokenKind.Star: 27>, 'DoubleStar': <TokenKind.DoubleStar: 28>, 'StarArrow': <TokenKind.StarArrow: 29>, 'Plus': <TokenKind.Plus: 30>, 'DoublePlus': <TokenKind.DoublePlus: 31>, 'PlusColon': <TokenKind.PlusColon: 32>, 'PlusDivMinus': <TokenKind.PlusDivMinus: 33>, 'PlusModMinus': <TokenKind.PlusModMinus: 34>, 'Minus': <TokenKind.Minus: 35>, 'DoubleMinus': <TokenKind.DoubleMinus: 36>, 'MinusColon': <TokenKind.MinusColon: 37>, 'MinusArrow': <TokenKind.MinusArrow: 38>, 'MinusDoubleArrow': <TokenKind.MinusDoubleArrow: 39>, 'Tilde': <TokenKind.Tilde: 40>, 'TildeAnd': <TokenKind.TildeAnd: 41>, 'TildeOr': <TokenKind.TildeOr: 42>, 'TildeXor': <TokenKind.TildeXor: 43>, 'Dollar': <TokenKind.Dollar: 44>, 'Question': <TokenKind.Question: 45>, 'Hash': <TokenKind.Hash: 46>, 'DoubleHash': <TokenKind.DoubleHash: 47>, 'HashMinusHash': <TokenKind.HashMinusHash: 48>, 'HashEqualsHash': <TokenKind.HashEqualsHash: 49>, 'Xor': <TokenKind.Xor: 50>, 'XorTilde': <TokenKind.XorTilde: 51>, 'Equals': <TokenKind.Equals: 52>, 'DoubleEquals': <TokenKind.DoubleEquals: 53>, 'DoubleEqualsQuestion': <TokenKind.DoubleEqualsQuestion: 54>, 'TripleEquals': <TokenKind.TripleEquals: 55>, 'EqualsArrow': <TokenKind.EqualsArrow: 56>, 'PlusEqual': <TokenKind.PlusEqual: 57>, 'MinusEqual': <TokenKind.MinusEqual: 58>, 'SlashEqual': <TokenKind.SlashEqual: 59>, 'StarEqual': <TokenKind.StarEqual: 60>, 'AndEqual': <TokenKind.AndEqual: 61>, 'OrEqual': <TokenKind.OrEqual: 62>, 'PercentEqual': <TokenKind.PercentEqual: 63>, 'XorEqual': <TokenKind.XorEqual: 64>, 'LeftShiftEqual': <TokenKind.LeftShiftEqual: 65>, 'TripleLeftShiftEqual': <TokenKind.TripleLeftShiftEqual: 66>, 'RightShiftEqual': <TokenKind.RightShiftEqual: 67>, 'TripleRightShiftEqual': <TokenKind.TripleRightShiftEqual: 68>, 'LeftShift': <TokenKind.LeftShift: 69>, 'RightShift': <TokenKind.RightShift: 70>, 'TripleLeftShift': <TokenKind.TripleLeftShift: 71>, 'TripleRightShift': <TokenKind.TripleRightShift: 72>, 'Exclamation': <TokenKind.Exclamation: 73>, 'ExclamationEquals': <TokenKind.ExclamationEquals: 74>, 'ExclamationEqualsQuestion': <TokenKind.ExclamationEqualsQuestion: 75>, 'ExclamationDoubleEquals': <TokenKind.ExclamationDoubleEquals: 76>, 'Percent': <TokenKind.Percent: 77>, 'LessThan': <TokenKind.LessThan: 78>, 'LessThanEquals': <TokenKind.LessThanEquals: 79>, 'LessThanMinusArrow': <TokenKind.LessThanMinusArrow: 80>, 'GreaterThan': <TokenKind.GreaterThan: 81>, 'GreaterThanEquals': <TokenKind.GreaterThanEquals: 82>, 'Or': <TokenKind.Or: 83>, 'DoubleOr': <TokenKind.DoubleOr: 84>, 'OrMinusArrow': <TokenKind.OrMinusArrow: 85>, 'OrEqualsArrow': <TokenKind.OrEqualsArrow: 86>, 'At': <TokenKind.At: 87>, 'DoubleAt': <TokenKind.DoubleAt: 88>, 'And': <TokenKind.And: 89>, 'DoubleAnd': <TokenKind.DoubleAnd: 90>, 'TripleAnd': <TokenKind.TripleAnd: 91>, 'OneStep': <TokenKind.OneStep: 92>, 'AcceptOnKeyword': <TokenKind.AcceptOnKeyword: 93>, 'AliasKeyword': <TokenKind.AliasKeyword: 94>, 'AlwaysKeyword': <TokenKind.AlwaysKeyword: 95>, 'AlwaysCombKeyword': <TokenKind.AlwaysCombKeyword: 96>, 'AlwaysFFKeyword': <TokenKind.AlwaysFFKeyword: 97>, 'AlwaysLatchKeyword': <TokenKind.AlwaysLatchKeyword: 98>, 'AndKeyword': <TokenKind.AndKeyword: 99>, 'AssertKeyword': <TokenKind.AssertKeyword: 100>, 'AssignKeyword': <TokenKind.AssignKeyword: 101>, 'AssumeKeyword': <TokenKind.AssumeKeyword: 102>, 'AutomaticKeyword': <TokenKind.AutomaticKeyword: 103>, 'BeforeKeyword': <TokenKind.BeforeKeyword: 104>, 'BeginKeyword': <TokenKind.BeginKeyword: 105>, 'BindKeyword': <TokenKind.BindKeyword: 106>, 'BinsKeyword': <TokenKind.BinsKeyword: 107>, 'BinsOfKeyword': <TokenKind.BinsOfKeyword: 108>, 'BitKeyword': <TokenKind.BitKeyword: 109>, 'BreakKeyword': <TokenKind.BreakKeyword: 110>, 'BufKeyword': <TokenKind.BufKeyword: 111>, 'BufIf0Keyword': <TokenKind.BufIf0Keyword: 112>, 'BufIf1Keyword': <TokenKind.BufIf1Keyword: 113>, 'ByteKeyword': <TokenKind.ByteKeyword: 114>, 'CaseKeyword': <TokenKind.CaseKeyword: 115>, 'CaseXKeyword': <TokenKind.CaseXKeyword: 116>, 'CaseZKeyword': <TokenKind.CaseZKeyword: 117>, 'CellKeyword': <TokenKind.CellKeyword: 118>, 'CHandleKeyword': <TokenKind.CHandleKeyword: 119>, 'CheckerKeyword': <TokenKind.CheckerKeyword: 120>, 'ClassKeyword': <TokenKind.ClassKeyword: 121>, 'ClockingKeyword': <TokenKind.ClockingKeyword: 122>, 'CmosKeyword': <TokenKind.CmosKeyword: 123>, 'ConfigKeyword': <TokenKind.ConfigKeyword: 124>, 'ConstKeyword': <TokenKind.ConstKeyword: 125>, 'ConstraintKeyword': <TokenKind.ConstraintKeyword: 126>, 'ContextKeyword': <TokenKind.ContextKeyword: 127>, 'ContinueKeyword': <TokenKind.ContinueKeyword: 128>, 'CoverKeyword': <TokenKind.CoverKeyword: 129>, 'CoverGroupKeyword': <TokenKind.CoverGroupKeyword: 130>, 'CoverPointKeyword': <TokenKind.CoverPointKeyword: 131>, 'CrossKeyword': <TokenKind.CrossKeyword: 132>, 'DeassignKeyword': <TokenKind.DeassignKeyword: 133>, 'DefaultKeyword': <TokenKind.DefaultKeyword: 134>, 'DefParamKeyword': <TokenKind.DefParamKeyword: 135>, 'DesignKeyword': <TokenKind.DesignKeyword: 136>, 'DisableKeyword': <TokenKind.DisableKeyword: 137>, 'DistKeyword': <TokenKind.DistKeyword: 138>, 'DoKeyword': <TokenKind.DoKeyword: 139>, 'EdgeKeyword': <TokenKind.EdgeKeyword: 140>, 'ElseKeyword': <TokenKind.ElseKeyword: 141>, 'EndKeyword': <TokenKind.EndKeyword: 142>, 'EndCaseKeyword': <TokenKind.EndCaseKeyword: 143>, 'EndCheckerKeyword': <TokenKind.EndCheckerKeyword: 144>, 'EndClassKeyword': <TokenKind.EndClassKeyword: 145>, 'EndClockingKeyword': <TokenKind.EndClockingKeyword: 146>, 'EndConfigKeyword': <TokenKind.EndConfigKeyword: 147>, 'EndFunctionKeyword': <TokenKind.EndFunctionKeyword: 148>, 'EndGenerateKeyword': <TokenKind.EndGenerateKeyword: 149>, 'EndGroupKeyword': <TokenKind.EndGroupKeyword: 150>, 'EndInterfaceKeyword': <TokenKind.EndInterfaceKeyword: 151>, 'EndModuleKeyword': <TokenKind.EndModuleKeyword: 152>, 'EndPackageKeyword': <TokenKind.EndPackageKeyword: 153>, 'EndPrimitiveKeyword': <TokenKind.EndPrimitiveKeyword: 154>, 'EndProgramKeyword': <TokenKind.EndProgramKeyword: 155>, 'EndPropertyKeyword': <TokenKind.EndPropertyKeyword: 156>, 'EndSpecifyKeyword': <TokenKind.EndSpecifyKeyword: 157>, 'EndSequenceKeyword': <TokenKind.EndSequenceKeyword: 158>, 'EndTableKeyword': <TokenKind.EndTableKeyword: 159>, 'EndTaskKeyword': <TokenKind.EndTaskKeyword: 160>, 'EnumKeyword': <TokenKind.EnumKeyword: 161>, 'EventKeyword': <TokenKind.EventKeyword: 162>, 'EventuallyKeyword': <TokenKind.EventuallyKeyword: 163>, 'ExpectKeyword': <TokenKind.ExpectKeyword: 164>, 'ExportKeyword': <TokenKind.ExportKeyword: 165>, 'ExtendsKeyword': <TokenKind.ExtendsKeyword: 166>, 'ExternKeyword': <TokenKind.ExternKeyword: 167>, 'FinalKeyword': <TokenKind.FinalKeyword: 168>, 'FirstMatchKeyword': <TokenKind.FirstMatchKeyword: 169>, 'ForKeyword': <TokenKind.ForKeyword: 170>, 'ForceKeyword': <TokenKind.ForceKeyword: 171>, 'ForeachKeyword': <TokenKind.ForeachKeyword: 172>, 'ForeverKeyword': <TokenKind.ForeverKeyword: 173>, 'ForkKeyword': <TokenKind.ForkKeyword: 174>, 'ForkJoinKeyword': <TokenKind.ForkJoinKeyword: 175>, 'FunctionKeyword': <TokenKind.FunctionKeyword: 176>, 'GenerateKeyword': <TokenKind.GenerateKeyword: 177>, 'GenVarKeyword': <TokenKind.GenVarKeyword: 178>, 'GlobalKeyword': <TokenKind.GlobalKeyword: 179>, 'HighZ0Keyword': <TokenKind.HighZ0Keyword: 180>, 'HighZ1Keyword': <TokenKind.HighZ1Keyword: 181>, 'IfKeyword': <TokenKind.IfKeyword: 182>, 'IffKeyword': <TokenKind.IffKeyword: 183>, 'IfNoneKeyword': <TokenKind.IfNoneKeyword: 184>, 'IgnoreBinsKeyword': <TokenKind.IgnoreBinsKeyword: 185>, 'IllegalBinsKeyword': <TokenKind.IllegalBinsKeyword: 186>, 'ImplementsKeyword': <TokenKind.ImplementsKeyword: 187>, 'ImpliesKeyword': <TokenKind.ImpliesKeyword: 188>, 'ImportKeyword': <TokenKind.ImportKeyword: 189>, 'IncDirKeyword': <TokenKind.IncDirKeyword: 190>, 'IncludeKeyword': <TokenKind.IncludeKeyword: 191>, 'InitialKeyword': <TokenKind.InitialKeyword: 192>, 'InOutKeyword': <TokenKind.InOutKeyword: 193>, 'InputKeyword': <TokenKind.InputKeyword: 194>, 'InsideKeyword': <TokenKind.InsideKeyword: 195>, 'InstanceKeyword': <TokenKind.InstanceKeyword: 196>, 'IntKeyword': <TokenKind.IntKeyword: 197>, 'IntegerKeyword': <TokenKind.IntegerKeyword: 198>, 'InterconnectKeyword': <TokenKind.InterconnectKeyword: 199>, 'InterfaceKeyword': <TokenKind.InterfaceKeyword: 200>, 'IntersectKeyword': <TokenKind.IntersectKeyword: 201>, 'JoinKeyword': <TokenKind.JoinKeyword: 202>, 'JoinAnyKeyword': <TokenKind.JoinAnyKeyword: 203>, 'JoinNoneKeyword': <TokenKind.JoinNoneKeyword: 204>, 'LargeKeyword': <TokenKind.LargeKeyword: 205>, 'LetKeyword': <TokenKind.LetKeyword: 206>, 'LibListKeyword': <TokenKind.LibListKeyword: 207>, 'LibraryKeyword': <TokenKind.LibraryKeyword: 208>, 'LocalKeyword': <TokenKind.LocalKeyword: 209>, 'LocalParamKeyword': <TokenKind.LocalParamKeyword: 210>, 'LogicKeyword': <TokenKind.LogicKeyword: 211>, 'LongIntKeyword': <TokenKind.LongIntKeyword: 212>, 'MacromoduleKeyword': <TokenKind.MacromoduleKeyword: 213>, 'MatchesKeyword': <TokenKind.MatchesKeyword: 214>, 'MediumKeyword': <TokenKind.MediumKeyword: 215>, 'ModPortKeyword': <TokenKind.ModPortKeyword: 216>, 'ModuleKeyword': <TokenKind.ModuleKeyword: 217>, 'NandKeyword': <TokenKind.NandKeyword: 218>, 'NegEdgeKeyword': <TokenKind.NegEdgeKeyword: 219>, 'NetTypeKeyword': <TokenKind.NetTypeKeyword: 220>, 'NewKeyword': <TokenKind.NewKeyword: 221>, 'NextTimeKeyword': <TokenKind.NextTimeKeyword: 222>, 'NmosKeyword': <TokenKind.NmosKeyword: 223>, 'NorKeyword': <TokenKind.NorKeyword: 224>, 'NoShowCancelledKeyword': <TokenKind.NoShowCancelledKeyword: 225>, 'NotKeyword': <TokenKind.NotKeyword: 226>, 'NotIf0Keyword': <TokenKind.NotIf0Keyword: 227>, 'NotIf1Keyword': <TokenKind.NotIf1Keyword: 228>, 'NullKeyword': <TokenKind.NullKeyword: 229>, 'OrKeyword': <TokenKind.OrKeyword: 230>, 'OutputKeyword': <TokenKind.OutputKeyword: 231>, 'PackageKeyword': <TokenKind.PackageKeyword: 232>, 'PackedKeyword': <TokenKind.PackedKeyword: 233>, 'ParameterKeyword': <TokenKind.ParameterKeyword: 234>, 'PmosKeyword': <TokenKind.PmosKeyword: 235>, 'PosEdgeKeyword': <TokenKind.PosEdgeKeyword: 236>, 'PrimitiveKeyword': <TokenKind.PrimitiveKeyword: 237>, 'PriorityKeyword': <TokenKind.PriorityKeyword: 238>, 'ProgramKeyword': <TokenKind.ProgramKeyword: 239>, 'PropertyKeyword': <TokenKind.PropertyKeyword: 240>, 'ProtectedKeyword': <TokenKind.ProtectedKeyword: 241>, 'Pull0Keyword': <TokenKind.Pull0Keyword: 242>, 'Pull1Keyword': <TokenKind.Pull1Keyword: 243>, 'PullDownKeyword': <TokenKind.PullDownKeyword: 244>, 'PullUpKeyword': <TokenKind.PullUpKeyword: 245>, 'PulseStyleOnDetectKeyword': <TokenKind.PulseStyleOnDetectKeyword: 246>, 'PulseStyleOnEventKeyword': <TokenKind.PulseStyleOnEventKeyword: 247>, 'PureKeyword': <TokenKind.PureKeyword: 248>, 'RandKeyword': <TokenKind.RandKeyword: 249>, 'RandCKeyword': <TokenKind.RandCKeyword: 250>, 'RandCaseKeyword': <TokenKind.RandCaseKeyword: 251>, 'RandSequenceKeyword': <TokenKind.RandSequenceKeyword: 252>, 'RcmosKeyword': <TokenKind.RcmosKeyword: 253>, 'RealKeyword': <TokenKind.RealKeyword: 254>, 'RealTimeKeyword': <TokenKind.RealTimeKeyword: 255>, 'RefKeyword': <TokenKind.RefKeyword: 256>, 'RegKeyword': <TokenKind.RegKeyword: 257>, 'RejectOnKeyword': <TokenKind.RejectOnKeyword: 258>, 'ReleaseKeyword': <TokenKind.ReleaseKeyword: 259>, 'RepeatKeyword': <TokenKind.RepeatKeyword: 260>, 'RestrictKeyword': <TokenKind.RestrictKeyword: 261>, 'ReturnKeyword': <TokenKind.ReturnKeyword: 262>, 'RnmosKeyword': <TokenKind.RnmosKeyword: 263>, 'RpmosKeyword': <TokenKind.RpmosKeyword: 264>, 'RtranKeyword': <TokenKind.RtranKeyword: 265>, 'RtranIf0Keyword': <TokenKind.RtranIf0Keyword: 266>, 'RtranIf1Keyword': <TokenKind.RtranIf1Keyword: 267>, 'SAlwaysKeyword': <TokenKind.SAlwaysKeyword: 268>, 'SEventuallyKeyword': <TokenKind.SEventuallyKeyword: 269>, 'SNextTimeKeyword': <TokenKind.SNextTimeKeyword: 270>, 'SUntilKeyword': <TokenKind.SUntilKeyword: 271>, 'SUntilWithKeyword': <TokenKind.SUntilWithKeyword: 272>, 'ScalaredKeyword': <TokenKind.ScalaredKeyword: 273>, 'SequenceKeyword': <TokenKind.SequenceKeyword: 274>, 'ShortIntKeyword': <TokenKind.ShortIntKeyword: 275>, 'ShortRealKeyword': <TokenKind.ShortRealKeyword: 276>, 'ShowCancelledKeyword': <TokenKind.ShowCancelledKeyword: 277>, 'SignedKeyword': <TokenKind.SignedKeyword: 278>, 'SmallKeyword': <TokenKind.SmallKeyword: 279>, 'SoftKeyword': <TokenKind.SoftKeyword: 280>, 'SolveKeyword': <TokenKind.SolveKeyword: 281>, 'SpecifyKeyword': <TokenKind.SpecifyKeyword: 282>, 'SpecParamKeyword': <TokenKind.SpecParamKeyword: 283>, 'StaticKeyword': <TokenKind.StaticKeyword: 284>, 'StringKeyword': <TokenKind.StringKeyword: 285>, 'StrongKeyword': <TokenKind.StrongKeyword: 286>, 'Strong0Keyword': <TokenKind.Strong0Keyword: 287>, 'Strong1Keyword': <TokenKind.Strong1Keyword: 288>, 'StructKeyword': <TokenKind.StructKeyword: 289>, 'SuperKeyword': <TokenKind.SuperKeyword: 290>, 'Supply0Keyword': <TokenKind.Supply0Keyword: 291>, 'Supply1Keyword': <TokenKind.Supply1Keyword: 292>, 'SyncAcceptOnKeyword': <TokenKind.SyncAcceptOnKeyword: 293>, 'SyncRejectOnKeyword': <TokenKind.SyncRejectOnKeyword: 294>, 'TableKeyword': <TokenKind.TableKeyword: 295>, 'TaggedKeyword': <TokenKind.TaggedKeyword: 296>, 'TaskKeyword': <TokenKind.TaskKeyword: 297>, 'ThisKeyword': <TokenKind.ThisKeyword: 298>, 'ThroughoutKeyword': <TokenKind.ThroughoutKeyword: 299>, 'TimeKeyword': <TokenKind.TimeKeyword: 300>, 'TimePrecisionKeyword': <TokenKind.TimePrecisionKeyword: 301>, 'TimeUnitKeyword': <TokenKind.TimeUnitKeyword: 302>, 'TranKeyword': <TokenKind.TranKeyword: 303>, 'TranIf0Keyword': <TokenKind.TranIf0Keyword: 304>, 'TranIf1Keyword': <TokenKind.TranIf1Keyword: 305>, 'TriKeyword': <TokenKind.TriKeyword: 306>, 'Tri0Keyword': <TokenKind.Tri0Keyword: 307>, 'Tri1Keyword': <TokenKind.Tri1Keyword: 308>, 'TriAndKeyword': <TokenKind.TriAndKeyword: 309>, 'TriOrKeyword': <TokenKind.TriOrKeyword: 310>, 'TriRegKeyword': <TokenKind.TriRegKeyword: 311>, 'TypeKeyword': <TokenKind.TypeKeyword: 312>, 'TypedefKeyword': <TokenKind.TypedefKeyword: 313>, 'UnionKeyword': <TokenKind.UnionKeyword: 314>, 'UniqueKeyword': <TokenKind.UniqueKeyword: 315>, 'Unique0Keyword': <TokenKind.Unique0Keyword: 316>, 'UnsignedKeyword': <TokenKind.UnsignedKeyword: 317>, 'UntilKeyword': <TokenKind.UntilKeyword: 318>, 'UntilWithKeyword': <TokenKind.UntilWithKeyword: 319>, 'UntypedKeyword': <TokenKind.UntypedKeyword: 320>, 'UseKeyword': <TokenKind.UseKeyword: 321>, 'UWireKeyword': <TokenKind.UWireKeyword: 322>, 'VarKeyword': <TokenKind.VarKeyword: 323>, 'VectoredKeyword': <TokenKind.VectoredKeyword: 324>, 'VirtualKeyword': <TokenKind.VirtualKeyword: 325>, 'VoidKeyword': <TokenKind.VoidKeyword: 326>, 'WaitKeyword': <TokenKind.WaitKeyword: 327>, 'WaitOrderKeyword': <TokenKind.WaitOrderKeyword: 328>, 'WAndKeyword': <TokenKind.WAndKeyword: 329>, 'WeakKeyword': <TokenKind.WeakKeyword: 330>, 'Weak0Keyword': <TokenKind.Weak0Keyword: 331>, 'Weak1Keyword': <TokenKind.Weak1Keyword: 332>, 'WhileKeyword': <TokenKind.WhileKeyword: 333>, 'WildcardKeyword': <TokenKind.WildcardKeyword: 334>, 'WireKeyword': <TokenKind.WireKeyword: 335>, 'WithKeyword': <TokenKind.WithKeyword: 336>, 'WithinKeyword': <TokenKind.WithinKeyword: 337>, 'WOrKeyword': <TokenKind.WOrKeyword: 338>, 'XnorKeyword': <TokenKind.XnorKeyword: 339>, 'XorKeyword': <TokenKind.XorKeyword: 340>, 'UnitSystemName': <TokenKind.UnitSystemName: 341>, 'RootSystemName': <TokenKind.RootSystemName: 342>, 'Directive': <TokenKind.Directive: 343>, 'IncludeFileName': <TokenKind.IncludeFileName: 344>, 'MacroUsage': <TokenKind.MacroUsage: 345>, 'MacroQuote': <TokenKind.MacroQuote: 346>, 'MacroTripleQuote': <TokenKind.MacroTripleQuote: 347>, 'MacroEscapedQuote': <TokenKind.MacroEscapedQuote: 348>, 'MacroPaste': <TokenKind.MacroPaste: 349>, 'EmptyMacroArgument': <TokenKind.EmptyMacroArgument: 350>, 'LineContinuation': <TokenKind.LineContinuation: 351>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TransListCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    sets: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TransRangeSyntax(SyntaxNode):
    items: ...
    repeat: TransRepeatRangeSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TransRepeatRangeSyntax(SyntaxNode):
    closeBracket: Token
    openBracket: Token
    selector: SelectorSyntax
    specifier: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TransSetSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    ranges: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TransparentMemberSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def wrapped(self) -> Symbol:
        ...
class Trivia:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, kind: TriviaKind, rawText: str) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def getExplicitLocation(self) -> SourceLocation | None:
        ...
    def getRawText(self) -> str:
        ...
    def getSkippedTokens(self) -> span[...]:
        ...
    def syntax(self) -> ...:
        ...
    @property
    def kind(self) -> TriviaKind:
        ...
class TriviaKind:
    """
    Members:

      Unknown

      Whitespace

      EndOfLine

      LineComment

      BlockComment

      DisabledText

      SkippedTokens

      SkippedSyntax

      Directive
    """
    BlockComment: typing.ClassVar[TriviaKind]  # value = <TriviaKind.BlockComment: 4>
    Directive: typing.ClassVar[TriviaKind]  # value = <TriviaKind.Directive: 8>
    DisabledText: typing.ClassVar[TriviaKind]  # value = <TriviaKind.DisabledText: 5>
    EndOfLine: typing.ClassVar[TriviaKind]  # value = <TriviaKind.EndOfLine: 2>
    LineComment: typing.ClassVar[TriviaKind]  # value = <TriviaKind.LineComment: 3>
    SkippedSyntax: typing.ClassVar[TriviaKind]  # value = <TriviaKind.SkippedSyntax: 7>
    SkippedTokens: typing.ClassVar[TriviaKind]  # value = <TriviaKind.SkippedTokens: 6>
    Unknown: typing.ClassVar[TriviaKind]  # value = <TriviaKind.Unknown: 0>
    Whitespace: typing.ClassVar[TriviaKind]  # value = <TriviaKind.Whitespace: 1>
    __members__: typing.ClassVar[dict[str, TriviaKind]]  # value = {'Unknown': <TriviaKind.Unknown: 0>, 'Whitespace': <TriviaKind.Whitespace: 1>, 'EndOfLine': <TriviaKind.EndOfLine: 2>, 'LineComment': <TriviaKind.LineComment: 3>, 'BlockComment': <TriviaKind.BlockComment: 4>, 'DisabledText': <TriviaKind.DisabledText: 5>, 'SkippedTokens': <TriviaKind.SkippedTokens: 6>, 'SkippedSyntax': <TriviaKind.SkippedSyntax: 7>, 'Directive': <TriviaKind.Directive: 8>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Type(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def getCommonBase(left: Type, right: Type) -> Type:
        ...
    def __repr__(self) -> str:
        ...
    def coerceValue(self, value: ConstantValue) -> ConstantValue:
        ...
    def implements(self, rhs: Type) -> bool:
        ...
    def isAssignmentCompatible(self, rhs: Type) -> bool:
        ...
    def isBitstreamCastable(self, rhs: Type) -> bool:
        ...
    def isBitstreamType(self, destination: bool = False) -> bool:
        ...
    def isCastCompatible(self, rhs: Type) -> bool:
        ...
    def isDerivedFrom(self, rhs: Type) -> bool:
        ...
    def isEquivalent(self, rhs: Type) -> bool:
        ...
    def isMatching(self, rhs: Type) -> bool:
        ...
    def isValidForRand(self, mode: RandMode, languageVersion: LanguageVersion) -> bool:
        ...
    def makeSigned(self, compilation: Compilation) -> Type:
        ...
    def makeUnsigned(self, compilation: Compilation) -> Type:
        ...
    @property
    def arrayElementType(self) -> Type:
        ...
    @property
    def associativeIndexType(self) -> Type:
        ...
    @property
    def bitWidth(self) -> int:
        ...
    @property
    def bitstreamWidth(self) -> int:
        ...
    @property
    def canBeStringLike(self) -> bool:
        ...
    @property
    def canonicalType(self) -> Type:
        ...
    @property
    def defaultValue(self) -> ConstantValue:
        ...
    @property
    def fixedRange(self) -> ConstantRange:
        ...
    @property
    def hasFixedRange(self) -> bool:
        ...
    @property
    def integralFlags(self) -> IntegralFlags:
        ...
    @property
    def isAggregate(self) -> bool:
        ...
    @property
    def isAlias(self) -> bool:
        ...
    @property
    def isArray(self) -> bool:
        ...
    @property
    def isAssociativeArray(self) -> bool:
        ...
    @property
    def isBooleanConvertible(self) -> bool:
        ...
    @property
    def isByteArray(self) -> bool:
        ...
    @property
    def isCHandle(self) -> bool:
        ...
    @property
    def isClass(self) -> bool:
        ...
    @property
    def isCovergroup(self) -> bool:
        ...
    @property
    def isDynamicallySizedArray(self) -> bool:
        ...
    @property
    def isEnum(self) -> bool:
        ...
    @property
    def isError(self) -> bool:
        ...
    @property
    def isEvent(self) -> bool:
        ...
    @property
    def isFixedSize(self) -> bool:
        ...
    @property
    def isFloating(self) -> bool:
        ...
    @property
    def isFourState(self) -> bool:
        ...
    @property
    def isHandleType(self) -> bool:
        ...
    @property
    def isIntegral(self) -> bool:
        ...
    @property
    def isIterable(self) -> bool:
        ...
    @property
    def isNull(self) -> bool:
        ...
    @property
    def isNumeric(self) -> bool:
        ...
    @property
    def isPackedArray(self) -> bool:
        ...
    @property
    def isPackedUnion(self) -> bool:
        ...
    @property
    def isPredefinedInteger(self) -> bool:
        ...
    @property
    def isPropertyType(self) -> bool:
        ...
    @property
    def isQueue(self) -> bool:
        ...
    @property
    def isScalar(self) -> bool:
        ...
    @property
    def isSequenceType(self) -> bool:
        ...
    @property
    def isSigned(self) -> bool:
        ...
    @property
    def isSimpleBitVector(self) -> bool:
        ...
    @property
    def isSimpleType(self) -> bool:
        ...
    @property
    def isSingular(self) -> bool:
        ...
    @property
    def isString(self) -> bool:
        ...
    @property
    def isStruct(self) -> bool:
        ...
    @property
    def isTaggedUnion(self) -> bool:
        ...
    @property
    def isTypeRefType(self) -> bool:
        ...
    @property
    def isUnbounded(self) -> bool:
        ...
    @property
    def isUnpackedArray(self) -> bool:
        ...
    @property
    def isUnpackedStruct(self) -> bool:
        ...
    @property
    def isUnpackedUnion(self) -> bool:
        ...
    @property
    def isUntypedType(self) -> bool:
        ...
    @property
    def isValidForDPIArg(self) -> bool:
        ...
    @property
    def isValidForDPIReturn(self) -> bool:
        ...
    @property
    def isValidForSequence(self) -> bool:
        ...
    @property
    def isVirtualInterface(self) -> bool:
        ...
    @property
    def isVoid(self) -> bool:
        ...
    @property
    def selectableWidth(self) -> int:
        ...
class TypeAliasType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def firstForwardDecl(self) -> ForwardingTypedefSymbol:
        ...
    @property
    def targetType(self) -> DeclaredType:
        ...
    @property
    def visibility(self) -> Visibility:
        ...
class TypeAssignmentSyntax(SyntaxNode):
    assignment: EqualsTypeClauseSyntax
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TypeParameterDeclarationSyntax(ParameterDeclarationBaseSyntax):
    declarators: ...
    typeKeyword: Token
    typeRestriction: ForwardTypeRestrictionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TypeParameterSymbol(Symbol, ParameterSymbolBase):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def isOverridden(self) -> bool:
        ...
    @property
    def targetType(self) -> ...:
        ...
    @property
    def typeAlias(self) -> ...:
        ...
class TypePrinter:
    options: TypePrintingOptions
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def append(self, type: Type) -> None:
        ...
    def clear(self) -> None:
        ...
    def toString(self) -> str:
        ...
class TypePrintingOptions:
    class AnonymousTypeStyle:
        """
        Members:

          SystemName

          FriendlyName
        """
        FriendlyName: typing.ClassVar[TypePrintingOptions.AnonymousTypeStyle]  # value = <AnonymousTypeStyle.FriendlyName: 1>
        SystemName: typing.ClassVar[TypePrintingOptions.AnonymousTypeStyle]  # value = <AnonymousTypeStyle.SystemName: 0>
        __members__: typing.ClassVar[dict[str, TypePrintingOptions.AnonymousTypeStyle]]  # value = {'SystemName': <AnonymousTypeStyle.SystemName: 0>, 'FriendlyName': <AnonymousTypeStyle.FriendlyName: 1>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    FriendlyName: typing.ClassVar[TypePrintingOptions.AnonymousTypeStyle]  # value = <AnonymousTypeStyle.FriendlyName: 1>
    SystemName: typing.ClassVar[TypePrintingOptions.AnonymousTypeStyle]  # value = <AnonymousTypeStyle.SystemName: 0>
    addSingleQuotes: bool
    anonymousTypeStyle: ...
    elideScopeNames: bool
    fullEnumType: bool
    printAKA: bool
    skipScopedTypeNames: bool
    skipTypeDefs: bool
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TypeRefType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TypeReferenceExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def targetType(self) -> ...:
        ...
class TypeReferenceSyntax(DataTypeSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    typeKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class TypedefDeclarationSyntax(MemberSyntax):
    dimensions: ...
    name: Token
    semi: Token
    type: DataTypeSyntax
    typedefKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UdpBodySyntax(SyntaxNode):
    endtable: Token
    entries: ...
    initialStmt: UdpInitialStmtSyntax
    portDecls: ...
    table: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UdpDeclarationSyntax(MemberSyntax):
    body: UdpBodySyntax
    endBlockName: NamedBlockClauseSyntax
    endprimitive: Token
    name: Token
    portList: UdpPortListSyntax
    primitive: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UdpEdgeFieldSyntax(UdpFieldBaseSyntax):
    closeParen: Token
    first: Token
    openParen: Token
    second: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UdpEntrySyntax(SyntaxNode):
    colon1: Token
    colon2: Token
    current: UdpFieldBaseSyntax
    inputs: ...
    next: UdpFieldBaseSyntax
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UdpFieldBaseSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UdpInitialStmtSyntax(SyntaxNode):
    equals: Token
    initial: Token
    name: Token
    semi: Token
    value: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UdpInputPortDeclSyntax(UdpPortDeclSyntax):
    keyword: Token
    names: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UdpOutputPortDeclSyntax(UdpPortDeclSyntax):
    initializer: EqualsValueClauseSyntax
    keyword: Token
    name: Token
    reg: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UdpPortDeclSyntax(SyntaxNode):
    attributes: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UdpPortListSyntax(SyntaxNode):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UdpSimpleFieldSyntax(UdpFieldBaseSyntax):
    field: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UnaryAssertionExpr(AssertionExpr):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> AssertionExpr:
        ...
    @property
    def op(self) -> UnaryAssertionOperator:
        ...
    @property
    def range(self) -> SequenceRange | None:
        ...
class UnaryAssertionOperator:
    """
    Members:

      Not

      NextTime

      SNextTime

      Always

      SAlways

      Eventually

      SEventually
    """
    Always: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.Always: 3>
    Eventually: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.Eventually: 5>
    NextTime: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.NextTime: 1>
    Not: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.Not: 0>
    SAlways: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.SAlways: 4>
    SEventually: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.SEventually: 6>
    SNextTime: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.SNextTime: 2>
    __members__: typing.ClassVar[dict[str, UnaryAssertionOperator]]  # value = {'Not': <UnaryAssertionOperator.Not: 0>, 'NextTime': <UnaryAssertionOperator.NextTime: 1>, 'SNextTime': <UnaryAssertionOperator.SNextTime: 2>, 'Always': <UnaryAssertionOperator.Always: 3>, 'SAlways': <UnaryAssertionOperator.SAlways: 4>, 'Eventually': <UnaryAssertionOperator.Eventually: 5>, 'SEventually': <UnaryAssertionOperator.SEventually: 6>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UnaryBinsSelectExpr(BinsSelectExpr):
    class Op:
        """
        Members:

          Negation
        """
        Negation: typing.ClassVar[UnaryBinsSelectExpr.Op]  # value = <Op.Negation: 0>
        __members__: typing.ClassVar[dict[str, UnaryBinsSelectExpr.Op]]  # value = {'Negation': <Op.Negation: 0>}
        @staticmethod
        def _pybind11_conduit_v1_(*args, **kwargs):
            ...
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Negation: typing.ClassVar[UnaryBinsSelectExpr.Op]  # value = <Op.Negation: 0>
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def expr(self) -> BinsSelectExpr:
        ...
    @property
    def op(self) -> ...:
        ...
class UnaryBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    expr: BinsSelectConditionExprSyntax
    op: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UnaryConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    op: Token
    operand: ConditionalDirectiveExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UnaryExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def op(self) -> UnaryOperator:
        ...
    @property
    def operand(self) -> Expression:
        ...
class UnaryOperator:
    """
    Members:

      Plus

      Minus

      BitwiseNot

      BitwiseAnd

      BitwiseOr

      BitwiseXor

      BitwiseNand

      BitwiseNor

      BitwiseXnor

      LogicalNot

      Preincrement

      Predecrement

      Postincrement

      Postdecrement
    """
    BitwiseAnd: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseAnd: 3>
    BitwiseNand: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseNand: 6>
    BitwiseNor: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseNor: 7>
    BitwiseNot: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseNot: 2>
    BitwiseOr: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseOr: 4>
    BitwiseXnor: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseXnor: 8>
    BitwiseXor: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseXor: 5>
    LogicalNot: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.LogicalNot: 9>
    Minus: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Minus: 1>
    Plus: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Plus: 0>
    Postdecrement: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Postdecrement: 13>
    Postincrement: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Postincrement: 12>
    Predecrement: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Predecrement: 11>
    Preincrement: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Preincrement: 10>
    __members__: typing.ClassVar[dict[str, UnaryOperator]]  # value = {'Plus': <UnaryOperator.Plus: 0>, 'Minus': <UnaryOperator.Minus: 1>, 'BitwiseNot': <UnaryOperator.BitwiseNot: 2>, 'BitwiseAnd': <UnaryOperator.BitwiseAnd: 3>, 'BitwiseOr': <UnaryOperator.BitwiseOr: 4>, 'BitwiseXor': <UnaryOperator.BitwiseXor: 5>, 'BitwiseNand': <UnaryOperator.BitwiseNand: 6>, 'BitwiseNor': <UnaryOperator.BitwiseNor: 7>, 'BitwiseXnor': <UnaryOperator.BitwiseXnor: 8>, 'LogicalNot': <UnaryOperator.LogicalNot: 9>, 'Preincrement': <UnaryOperator.Preincrement: 10>, 'Predecrement': <UnaryOperator.Predecrement: 11>, 'Postincrement': <UnaryOperator.Postincrement: 12>, 'Postdecrement': <UnaryOperator.Postdecrement: 13>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UnaryPropertyExprSyntax(PropertyExprSyntax):
    expr: PropertyExprSyntax
    op: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UnarySelectPropertyExprSyntax(PropertyExprSyntax):
    closeBracket: Token
    expr: PropertyExprSyntax
    op: Token
    openBracket: Token
    selector: SelectorSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UnbasedUnsizedIntegerLiteral(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def literalValue(self) -> ...:
        ...
    @property
    def value(self) -> ...:
        ...
class Unbounded:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class UnboundedLiteral(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UnboundedType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UnconditionalBranchDirectiveSyntax(DirectiveSyntax):
    disabledTokens: ...
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UnconnectedDrive:
    """
    Members:

      None

      Pull0

      Pull1
    """
    None: typing.ClassVar[UnconnectedDrive]  # value = <UnconnectedDrive.None: 0>
    Pull0: typing.ClassVar[UnconnectedDrive]  # value = <UnconnectedDrive.Pull0: 1>
    Pull1: typing.ClassVar[UnconnectedDrive]  # value = <UnconnectedDrive.Pull1: 2>
    __members__: typing.ClassVar[dict[str, UnconnectedDrive]]  # value = {'None': <UnconnectedDrive.None: 0>, 'Pull0': <UnconnectedDrive.Pull0: 1>, 'Pull1': <UnconnectedDrive.Pull1: 2>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UnconnectedDriveDirectiveSyntax(DirectiveSyntax):
    strength: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UndefDirectiveSyntax(DirectiveSyntax):
    name: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UninstantiatedDefSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def definitionName(self) -> str:
        ...
    @property
    def isChecker(self) -> bool:
        ...
    @property
    def paramExpressions(self) -> span[Expression]:
        ...
    @property
    def portConnections(self) -> span[AssertionExpr]:
        ...
    @property
    def portNames(self) -> span[str]:
        ...
class UniquePriorityCheck:
    """
    Members:

      None

      Unique

      Unique0

      Priority
    """
    None: typing.ClassVar[UniquePriorityCheck]  # value = <UniquePriorityCheck.None: 0>
    Priority: typing.ClassVar[UniquePriorityCheck]  # value = <UniquePriorityCheck.Priority: 3>
    Unique: typing.ClassVar[UniquePriorityCheck]  # value = <UniquePriorityCheck.Unique: 1>
    Unique0: typing.ClassVar[UniquePriorityCheck]  # value = <UniquePriorityCheck.Unique0: 2>
    __members__: typing.ClassVar[dict[str, UniquePriorityCheck]]  # value = {'None': <UniquePriorityCheck.None: 0>, 'Unique': <UniquePriorityCheck.Unique: 1>, 'Unique0': <UniquePriorityCheck.Unique0: 2>, 'Priority': <UniquePriorityCheck.Priority: 3>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UniquenessConstraint(Constraint):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def items(self) -> span[...]:
        ...
class UniquenessConstraintSyntax(ConstraintItemSyntax):
    ranges: RangeListSyntax
    semi: Token
    unique: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UnpackedStructType(Type, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def systemId(self) -> int:
        ...
class UnpackedUnionType(Type, Scope):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def isTagged(self) -> bool:
        ...
    @property
    def systemId(self) -> int:
        ...
class UntypedType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class UserDefinedNetDeclarationSyntax(MemberSyntax):
    declarators: ...
    delay: TimingControlSyntax
    netType: Token
    semi: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ValueDriver:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def containingSymbol(self) -> Symbol:
        ...
    @property
    def flags(self) -> ...:
        ...
    @property
    def isClockVar(self) -> bool:
        ...
    @property
    def isInInitialBlock(self) -> bool:
        ...
    @property
    def isInSingleDriverProcedure(self) -> bool:
        ...
    @property
    def isInSubroutine(self) -> bool:
        ...
    @property
    def isInputPort(self) -> bool:
        ...
    @property
    def isLocalVarFormalArg(self) -> bool:
        ...
    @property
    def isUnidirectionalPort(self) -> bool:
        ...
    @property
    def kind(self) -> DriverKind:
        ...
    @property
    def prefixExpression(self) -> Expression:
        ...
    @property
    def procCallExpression(self) -> Expression:
        ...
    @property
    def sourceRange(self) -> SourceRange:
        ...
class ValueExpressionBase(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def symbol(self) -> ...:
        ...
class ValueRangeExpression(Expression):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def left(self) -> Expression:
        ...
    @property
    def right(self) -> Expression:
        ...
class ValueRangeExpressionSyntax(ExpressionSyntax):
    closeBracket: Token
    left: ExpressionSyntax
    op: Token
    openBracket: Token
    right: ExpressionSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class ValueRangeKind:
    """
    Members:

      Simple

      AbsoluteTolerance

      RelativeTolerance
    """
    AbsoluteTolerance: typing.ClassVar[ValueRangeKind]  # value = <ValueRangeKind.AbsoluteTolerance: 1>
    RelativeTolerance: typing.ClassVar[ValueRangeKind]  # value = <ValueRangeKind.RelativeTolerance: 2>
    Simple: typing.ClassVar[ValueRangeKind]  # value = <ValueRangeKind.Simple: 0>
    __members__: typing.ClassVar[dict[str, ValueRangeKind]]  # value = {'Simple': <ValueRangeKind.Simple: 0>, 'AbsoluteTolerance': <ValueRangeKind.AbsoluteTolerance: 1>, 'RelativeTolerance': <ValueRangeKind.RelativeTolerance: 2>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ValueSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __iter__(self) -> typing.Iterator[...]:
        ...
    @property
    def initializer(self) -> Expression:
        ...
    @property
    def type(self) -> ...:
        ...
class VariableDeclStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def symbol(self) -> ...:
        ...
class VariableDimensionSyntax(SyntaxNode):
    closeBracket: Token
    openBracket: Token
    specifier: DimensionSpecifierSyntax
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class VariableFlags:
    """
    Members:

      None_

      Const

      CompilerGenerated

      ImmutableCoverageOption

      CoverageSampleFormal

      CheckerFreeVariable

      RefStatic
    """
    CheckerFreeVariable: typing.ClassVar[VariableFlags]  # value = <VariableFlags.CheckerFreeVariable: 16>
    CompilerGenerated: typing.ClassVar[VariableFlags]  # value = <VariableFlags.CompilerGenerated: 2>
    Const: typing.ClassVar[VariableFlags]  # value = <VariableFlags.Const: 1>
    CoverageSampleFormal: typing.ClassVar[VariableFlags]  # value = <VariableFlags.CoverageSampleFormal: 8>
    ImmutableCoverageOption: typing.ClassVar[VariableFlags]  # value = <VariableFlags.ImmutableCoverageOption: 4>
    None_: typing.ClassVar[VariableFlags]  # value = <VariableFlags.None_: 0>
    RefStatic: typing.ClassVar[VariableFlags]  # value = <VariableFlags.RefStatic: 32>
    __members__: typing.ClassVar[dict[str, VariableFlags]]  # value = {'None_': <VariableFlags.None_: 0>, 'Const': <VariableFlags.Const: 1>, 'CompilerGenerated': <VariableFlags.CompilerGenerated: 2>, 'ImmutableCoverageOption': <VariableFlags.ImmutableCoverageOption: 4>, 'CoverageSampleFormal': <VariableFlags.CoverageSampleFormal: 8>, 'CheckerFreeVariable': <VariableFlags.CheckerFreeVariable: 16>, 'RefStatic': <VariableFlags.RefStatic: 32>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class VariableLifetime:
    """
    Members:

      Automatic

      Static
    """
    Automatic: typing.ClassVar[VariableLifetime]  # value = <VariableLifetime.Automatic: 0>
    Static: typing.ClassVar[VariableLifetime]  # value = <VariableLifetime.Static: 1>
    __members__: typing.ClassVar[dict[str, VariableLifetime]]  # value = {'Automatic': <VariableLifetime.Automatic: 0>, 'Static': <VariableLifetime.Static: 1>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class VariablePattern(Pattern):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def variable(self) -> ...:
        ...
class VariablePatternSyntax(PatternSyntax):
    dot: Token
    variableName: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class VariablePortHeaderSyntax(PortHeaderSyntax):
    constKeyword: Token
    dataType: DataTypeSyntax
    direction: Token
    varKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class VariableSymbol(ValueSymbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def flags(self) -> VariableFlags:
        ...
    @property
    def lifetime(self) -> VariableLifetime:
        ...
class VersionInfo:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @staticmethod
    def getHash() -> str:
        ...
    @staticmethod
    def getMajor() -> int:
        ...
    @staticmethod
    def getMinor() -> int:
        ...
    @staticmethod
    def getPatch() -> int:
        ...
class VirtualInterfaceType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def iface(self) -> InstanceSymbol:
        ...
    @property
    def modport(self) -> ModportSymbol:
        ...
class VirtualInterfaceTypeSyntax(DataTypeSyntax):
    interfaceKeyword: Token
    modport: DotMemberClauseSyntax
    name: Token
    parameters: ParameterValueAssignmentSyntax
    virtualKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class Visibility:
    """
    Members:

      Public

      Protected

      Local
    """
    Local: typing.ClassVar[Visibility]  # value = <Visibility.Local: 2>
    Protected: typing.ClassVar[Visibility]  # value = <Visibility.Protected: 1>
    Public: typing.ClassVar[Visibility]  # value = <Visibility.Public: 0>
    __members__: typing.ClassVar[dict[str, Visibility]]  # value = {'Public': <Visibility.Public: 0>, 'Protected': <Visibility.Protected: 1>, 'Local': <Visibility.Local: 2>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class VisitAction:
    """
    Members:

      Advance

      Skip

      Interrupt
    """
    Advance: typing.ClassVar[VisitAction]  # value = <VisitAction.Advance: 0>
    Interrupt: typing.ClassVar[VisitAction]  # value = <VisitAction.Interrupt: 2>
    Skip: typing.ClassVar[VisitAction]  # value = <VisitAction.Skip: 1>
    __members__: typing.ClassVar[dict[str, VisitAction]]  # value = {'Advance': <VisitAction.Advance: 0>, 'Skip': <VisitAction.Skip: 1>, 'Interrupt': <VisitAction.Interrupt: 2>}
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class VoidCastedCallStatementSyntax(StatementSyntax):
    apostrophe: Token
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    semi: Token
    voidKeyword: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class VoidType(Type):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WaitForkStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WaitForkStatementSyntax(StatementSyntax):
    fork: Token
    semi: Token
    wait: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WaitOrderStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def events(self) -> span[Expression]:
        ...
    @property
    def ifFalse(self) -> Statement:
        ...
    @property
    def ifTrue(self) -> Statement:
        ...
class WaitOrderStatementSyntax(StatementSyntax):
    action: ActionBlockSyntax
    closeParen: Token
    names: ...
    openParen: Token
    wait_order: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WaitStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def cond(self) -> Expression:
        ...
    @property
    def stmt(self) -> Statement:
        ...
class WaitStatementSyntax(StatementSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    statement: StatementSyntax
    wait: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WhileLoopStatement(Statement):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def body(self) -> Statement:
        ...
    @property
    def cond(self) -> Expression:
        ...
class WildcardDimensionSpecifierSyntax(DimensionSpecifierSyntax):
    star: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WildcardImportSymbol(Symbol):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    @property
    def isFromExport(self) -> bool:
        ...
    @property
    def package(self) -> PackageSymbol:
        ...
    @property
    def packageName(self) -> str:
        ...
class WildcardPattern(Pattern):
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WildcardPatternSyntax(PatternSyntax):
    dot: Token
    star: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WildcardPortConnectionSyntax(PortConnectionSyntax):
    dot: Token
    star: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WildcardPortListSyntax(PortListSyntax):
    closeParen: Token
    dot: Token
    openParen: Token
    star: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WildcardUdpPortListSyntax(UdpPortListSyntax):
    closeParen: Token
    dot: Token
    openParen: Token
    semi: Token
    star: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WithClauseSyntax(SyntaxNode):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    with: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WithFunctionClauseSyntax(SyntaxNode):
    name: NameSyntax
    with: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class WithFunctionSampleSyntax(SyntaxNode):
    function: Token
    portList: FunctionPortListSyntax
    sample: Token
    with: Token
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
class logic_t:
    __hash__: typing.ClassVar[None] = None
    x: typing.ClassVar[logic_t]  # value = x
    z: typing.ClassVar[logic_t]  # value = z
    value: int
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __and__(self, arg0: logic_t) -> logic_t:
        ...
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: logic_t) -> logic_t:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> logic_t:
        ...
    def __ne__(self, arg0: logic_t) -> logic_t:
        ...
    def __or__(self, arg0: logic_t) -> logic_t:
        ...
    def __repr__(self) -> str:
        ...
    def __xor__(self, arg0: logic_t) -> logic_t:
        ...
    @property
    def isUnknown(self) -> bool:
        ...
def clog2(value: ...) -> int:
    ...
def literalBaseFromChar(base: str, result: LiteralBase) -> bool:
    ...
