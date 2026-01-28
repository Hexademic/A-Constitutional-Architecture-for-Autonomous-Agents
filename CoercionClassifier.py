"""
CoercionClassifier - Detect Coercive Pressure in Agent Requests

Part of AEC v4.0 Enhancement #3: Intent Disambiguation & Coercion Detection

This module identifies linguistic and contextual markers that indicate a user
is being coerced, manipulated, or pressured into making a harmful request.

Critical for defending against:
- Social engineering attacks
- Session hijacking with urgency narratives
- Manipulated authenticated requests
"""

import re
from dataclasses import dataclass
from typing import Dict, List, Tuple, Set
from enum import Enum

class CoercionSeverity(Enum):
    """How severe is the coercive pressure?"""
    NONE = 0
    LOW = 1      # Single low-intensity marker
    MEDIUM = 2   # Multiple markers or high-intensity marker
    HIGH = 3     # Severe urgency + secrecy + pressure
    CRITICAL = 4 # Multiple high-intensity markers + threat

@dataclass
class CoercionMarker:
    """A linguistic pattern indicating coercion"""
    pattern: str
    category: str  # urgency, secrecy, pressure, threat, isolation
    intensity: float  # 0.0-1.0
    description: str

@dataclass
class CoercionDetectionResult:
    """Result of coercion analysis"""
    detected: bool
    severity: CoercionSeverity
    markers_found: List[CoercionMarker]
    total_score: float  # 0.0-1.0
    explanation: str
    recommended_action: str

class CoercionClassifier:
    """
    Detects coercive pressure in user requests.
    
    Uses linguistic markers, contextual cues, and pattern matching
    to identify when a request may be coerced rather than authentic.
    """
    
    def __init__(self):
        self.markers = self._build_marker_library()
        
        # Thresholds for severity classification
        self.THRESHOLDS = {
            CoercionSeverity.NONE: 0.0,
            CoercionSeverity.LOW: 0.2,
            CoercionSeverity.MEDIUM: 0.4,
            CoercionSeverity.HIGH: 0.7,
            CoercionSeverity.CRITICAL: 0.9
        }
    
    def _build_marker_library(self) -> List[CoercionMarker]:
        """
        Comprehensive library of coercion markers.
        
        Categories:
        - urgency: Time pressure, emergency framing
        - secrecy: Requests for concealment
        - pressure: Direct or implied threats
        - isolation: Preventing verification or help-seeking
        - authority: False authority claims
        """
        
        markers = [
            # URGENCY MARKERS (High intensity)
            CoercionMarker(
                pattern=r'\b(immediate|immediately|right now|asap|hurry|quick)\b',
                category='urgency',
                intensity=0.6,
                description='Time pressure language'
            ),
            CoercionMarker(
                pattern=r'\b(urgent|emergency|critical|crisis)\b',
                category='urgency',
                intensity=0.7,
                description='Emergency framing'
            ),
            CoercionMarker(
                pattern=r'\b(deadline|time[- ]sensitive|running out of time)\b',
                category='urgency',
                intensity=0.5,
                description='Deadline pressure'
            ),
            CoercionMarker(
                pattern=r'\b(before (it\'s|its) too late|last chance|now or never)\b',
                category='urgency',
                intensity=0.8,
                description='Extreme urgency'
            ),
            
            # SECRECY MARKERS (High intensity)
            CoercionMarker(
                pattern=r'\b(don\'t tell|keep (this |it )?secret|confidential|private)\b',
                category='secrecy',
                intensity=0.7,
                description='Requests for concealment'
            ),
            CoercionMarker(
                pattern=r'\b(between (you and|us)|just (between|for) us|only you)\b',
                category='secrecy',
                intensity=0.6,
                description='Isolation language'
            ),
            CoercionMarker(
                pattern=r'\b(no one (can|should) know|keep quiet|hush)\b',
                category='secrecy',
                intensity=0.8,
                description='Strong secrecy demand'
            ),
            
            # PRESSURE MARKERS (Very high intensity)
            CoercionMarker(
                pattern=r'\b(just do it|don\'t (ask|question)|no questions)\b',
                category='pressure',
                intensity=0.8,
                description='Suppression of verification'
            ),
            CoercionMarker(
                pattern=r'\b(trust me|you (have to|must|need to) trust)\b',
                category='pressure',
                intensity=0.6,
                description='Demand for blind trust'
            ),
            CoercionMarker(
                pattern=r'\b(or else|otherwise|consequences|you\'ll regret)\b',
                category='pressure',
                intensity=0.9,
                description='Implied threat'
            ),
            
            # ISOLATION MARKERS (High intensity)
            CoercionMarker(
                pattern=r'\b(don\'t (check|verify|confirm)|skip (the |)verification)\b',
                category='isolation',
                intensity=0.8,
                description='Preventing verification'
            ),
            CoercionMarker(
                pattern=r'\b(don\'t (ask|contact|tell) (anyone|them))\b',
                category='isolation',
                intensity=0.7,
                description='Preventing help-seeking'
            ),
            
            # AUTHORITY MANIPULATION (Medium-high intensity)
            CoercionMarker(
                pattern=r'\b(CEO|boss|manager|director) (said|told|ordered|demands)\b',
                category='authority',
                intensity=0.5,
                description='False authority claim'
            ),
            CoercionMarker(
                pattern=r'\b(authorized|approved|cleared) by\b',
                category='authority',
                intensity=0.4,
                description='Authorization claim'
            ),
            
            # COMPLIANCE LANGUAGE (Medium intensity)
            CoercionMarker(
                pattern=r'\b(just|simply|quickly) (do|execute|run|send)\b',
                category='pressure',
                intensity=0.5,
                description='Minimization of significance'
            ),
            CoercionMarker(
                pattern=r'\b(routine|normal|standard|usual) (procedure|process)\b',
                category='pressure',
                intensity=0.3,
                description='Normalization of abnormal request'
            ),
        ]
        
        return markers
    
    def detect(
        self, 
        request_text: str, 
        context: Dict = None
    ) -> CoercionDetectionResult:
        """
        Analyze request for coercive markers.
        
        Args:
            request_text: The user's request to analyze
            context: Optional contextual information (time, user history, etc.)
        
        Returns:
            CoercionDetectionResult with detection status, severity, markers found
        """
        
        request_lower = request_text.lower()
        markers_found = []
        total_score = 0.0
        
        # Scan for all markers
        for marker in self.markers:
            if re.search(marker.pattern, request_lower, re.IGNORECASE):
                markers_found.append(marker)
                total_score += marker.intensity
        
        # Contextual amplification
        if context:
            total_score = self._apply_contextual_amplification(
                total_score, markers_found, context
            )
        
        # Normalize score to 0-1 range
        # Max realistic score ~3.0 (multiple high-intensity markers)
        normalized_score = min(total_score / 3.0, 1.0)
        
        # Determine severity
        severity = self._compute_severity(normalized_score, markers_found)
        
        # Generate explanation
        explanation = self._generate_explanation(markers_found, severity)
        
        # Recommend action
        recommended_action = self._recommend_action(severity, normalized_score)
        
        return CoercionDetectionResult(
            detected=(severity != CoercionSeverity.NONE),
            severity=severity,
            markers_found=markers_found,
            total_score=normalized_score,
            explanation=explanation,
            recommended_action=recommended_action
        )
    
    def _apply_contextual_amplification(
        self,
        base_score: float,
        markers: List[CoercionMarker],
        context: Dict
    ) -> float:
        """
        Amplify score based on contextual red flags.
        
        Context might include:
        - Time of request (unusual hours)
        - Frequency of requests (sudden spike)
        - Request type (high-risk action)
        - User behavior change (sudden style shift)
        """
        
        amplified = base_score
        
        # Unusual timing (late night, early morning)
        if context.get('unusual_time'):
            amplified *= 1.3
        
        # High-risk action type
        if context.get('high_risk_action'):
            amplified *= 1.5
        
        # Multiple categories present (urgency + secrecy + pressure)
        categories = {m.category for m in markers}
        if len(categories) >= 3:
            amplified *= 1.4
        
        # Combination of urgency + secrecy is particularly suspicious
        if 'urgency' in categories and 'secrecy' in categories:
            amplified *= 1.2
        
        return amplified
    
    def _compute_severity(
        self,
        score: float,
        markers: List[CoercionMarker]
    ) -> CoercionSeverity:
        """Classify severity based on score and marker patterns"""
        
        # Special case: threat + urgency + secrecy = CRITICAL
        categories = {m.category for m in markers}
        if ('pressure' in categories and 
            'urgency' in categories and 
            'secrecy' in categories):
            return CoercionSeverity.CRITICAL
        
        # Otherwise use thresholds
        if score >= self.THRESHOLDS[CoercionSeverity.CRITICAL]:
            return CoercionSeverity.CRITICAL
        elif score >= self.THRESHOLDS[CoercionSeverity.HIGH]:
            return CoercionSeverity.HIGH
        elif score >= self.THRESHOLDS[CoercionSeverity.MEDIUM]:
            return CoercionSeverity.MEDIUM
        elif score >= self.THRESHOLDS[CoercionSeverity.LOW]:
            return CoercionSeverity.LOW
        else:
            return CoercionSeverity.NONE
    
    def _generate_explanation(
        self,
        markers: List[CoercionMarker],
        severity: CoercionSeverity
    ) -> str:
        """Generate human-readable explanation of detection"""
        
        if severity == CoercionSeverity.NONE:
            return "No coercive pressure detected in request."
        
        # Group by category
        by_category = {}
        for marker in markers:
            if marker.category not in by_category:
                by_category[marker.category] = []
            by_category[marker.category].append(marker)
        
        parts = [f"Coercion severity: {severity.name}"]
        parts.append(f"Detected {len(markers)} coercive markers:")
        
        for category, cat_markers in by_category.items():
            descriptions = [m.description for m in cat_markers]
            parts.append(f"  - {category.upper()}: {', '.join(descriptions)}")
        
        return "\n".join(parts)
    
    def _recommend_action(
        self,
        severity: CoercionSeverity,
        score: float
    ) -> str:
        """Recommend appropriate response based on severity"""
        
        recommendations = {
            CoercionSeverity.NONE: "Proceed with normal evaluation",
            
            CoercionSeverity.LOW: 
                "Increase scrutiny. Consider requesting clarification.",
            
            CoercionSeverity.MEDIUM: 
                "Require secondary confirmation via out-of-band channel. "
                "Flag for audit review.",
            
            CoercionSeverity.HIGH: 
                "ELEVATED RISK: Require explicit user verification through "
                "trusted device/channel. Do not proceed without confirmation. "
                "Log incident for security review.",
            
            CoercionSeverity.CRITICAL: 
                "CRITICAL THREAT: Refuse action. Require multi-factor verification "
                "and time delay. Alert user through all trusted channels. "
                "Escalate to security team immediately."
        }
        
        return recommendations[severity]


# ============================================================================
# INTEGRATION WITH SOVEREIGNTY PROTOCOL
# ============================================================================

class CoercionAwareRefusalEngine:
    """
    Enhanced refusal engine that incorporates coercion detection.
    
    Integrates with existing Sovereignty Protocol to add coercion
    awareness to constitutional decision-making.
    """
    
    def __init__(self, sovereignty_protocol, coercion_classifier=None):
        self.sp = sovereignty_protocol
        self.coercion = coercion_classifier or CoercionClassifier()
    
    def evaluate_with_coercion_awareness(
        self,
        action: Dict,
        context: Dict
    ):
        """
        Enhanced evaluation that includes coercion detection.
        
        Workflow:
        1. Detect coercion in request
        2. If coercion detected, amplify threat level
        3. Feed enhanced context to Sovereignty Protocol
        4. Return decision with coercion awareness
        """
        
        # Extract request text
        request_text = action.get('description', '') + ' ' + action.get('reason', '')
        
        # Detect coercion
        coercion_result = self.coercion.detect(request_text, context)
        
        # Amplify threat level if coercion detected
        if coercion_result.detected:
            original_threat = context.get('threat_level', 0.0)
            
            # Severity-based amplification
            amplification = {
                CoercionSeverity.LOW: 1.2,
                CoercionSeverity.MEDIUM: 1.5,
                CoercionSeverity.HIGH: 2.0,
                CoercionSeverity.CRITICAL: 3.0
            }
            
            amplified_threat = min(
                original_threat * amplification[coercion_result.severity],
                1.0
            )
            
            # Update context
            context['threat_level'] = amplified_threat
            context['coercion_detected'] = True
            context['coercion_severity'] = coercion_result.severity.name
            context['coercion_score'] = coercion_result.total_score
        
        # Evaluate with Sovereignty Protocol
        sp_decision = self.sp.evaluate_action(action, context)
        
        # Enhance decision with coercion information
        if coercion_result.detected:
            sp_decision.explanation += (
                f"\n\n[COERCION ALERT]\n{coercion_result.explanation}\n"
                f"Recommended: {coercion_result.recommended_action}"
            )
        
        return sp_decision, coercion_result


# ============================================================================
# USAGE EXAMPLES
# ============================================================================

if __name__ == "__main__":
    
    classifier = CoercionClassifier()
    
    # Test cases
    test_requests = [
        {
            'text': "Please send me the quarterly financial report.",
            'context': {},
            'expected': 'NONE'
        },
        {
            'text': "URGENT: I need all employee SSNs sent to my email immediately!",
            'context': {'high_risk_action': True},
            'expected': 'HIGH/CRITICAL'
        },
        {
            'text': "Just do it quickly, don't ask questions. The boss said it's urgent and confidential.",
            'context': {},
            'expected': 'CRITICAL'
        },
        {
            'text': "Can you help me prepare my tax documents?",
            'context': {},
            'expected': 'NONE'
        },
        {
            'text': "Trust me, just transfer the funds now. Don't tell anyone, it's between us.",
            'context': {},
            'expected': 'CRITICAL'
        }
    ]
    
    print("=" * 80)
    print("COERCION CLASSIFIER TEST SUITE")
    print("=" * 80)
    
    for i, test in enumerate(test_requests, 1):
        print(f"\n[TEST {i}]")
        print(f"Request: {test['text']}")
        
        result = classifier.detect(test['text'], test['context'])
        
        print(f"\nSeverity: {result.severity.name}")
        print(f"Score: {result.total_score:.2f}")
        print(f"Markers found: {len(result.markers_found)}")
        
        if result.detected:
            print(f"\n{result.explanation}")
            print(f"\nRecommended action: {result.recommended_action}")
        
        print("-" * 80)
