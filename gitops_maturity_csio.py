
GITOPS_MATURITY = {
    "Level 1": "Manual CI/CD", 
    "Level 2": "GitHub Actions ✓",
    "Level 3": "ArgoCD Live ✓", 
    "Level 4": "Policy As Code ✓"
}
maturity = sum(i+1 for i,level in enumerate(GITOPS_MATURITY.values()) if "✓" in level)
print(f"GitOps Maturity: Level {maturity}/4 - Enterprise")

