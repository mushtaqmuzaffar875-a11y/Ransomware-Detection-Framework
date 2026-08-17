class RiskEngine:
    """Calculate ransomware detection risk from multiple signals."""

    def __init__(self):
        self.weights = {
            "mass_file_activity": 40,
            "high_entropy": 30,
            "suspicious_extension": 20,
            "rapid_renames": 10,
        }

    def calculate_score(
        self,
        mass_file_activity=False,
        high_entropy=False,
        suspicious_extension=False,
        rapid_renames=False,
    ):
        score = 0

        if mass_file_activity:
            score += self.weights["mass_file_activity"]

        if high_entropy:
            score += self.weights["high_entropy"]

        if suspicious_extension:
            score += self.weights["suspicious_extension"]

        if rapid_renames:
            score += self.weights["rapid_renames"]

        return min(score, 100)

    def get_risk_level(self, score):
        if score >= 90:
            return "CRITICAL"
        elif score >= 75:
            return "HIGH"
        elif score >= 50:
            return "MEDIUM"
        else:
            return "LOW"


if __name__ == "__main__":
    engine = RiskEngine()

    print("----- RISK ENGINE TEST -----")

    score = engine.calculate_score(
        mass_file_activity=True,
        high_entropy=True,
        suspicious_extension=True,
        rapid_renames=True,
    )

    level = engine.get_risk_level(score)

    print(f"Risk Score: {score}/100")
    print(f"Risk Level: {level}")
