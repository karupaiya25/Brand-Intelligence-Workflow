import reflex as rx


class CategoryScore(rx.Base):
    name: str
    score: int
    status: str
    color: str
    icon: str
    rationale: str


class Recommendation(rx.Base):
    category: str
    issue: str
    impact: str


class WebsiteAnalysisState(rx.State):
    overall_health_score: int = 72
    categories: list[CategoryScore] = [
        CategoryScore(
            name="AI Optimization",
            score=65,
            status="Fair",
            color="text-yellow-600",
            icon="bot",
            rationale="Content lacks sufficient density and semantic relationships for optimal LLM parsing.",
        ),
        CategoryScore(
            name="Structured Data",
            score=88,
            status="Good",
            color="text-green-600",
            icon="database",
            rationale="Rich snippets are correctly implemented for most product pages, enhancing visibility.",
        ),
        CategoryScore(
            name="Page Layout",
            score=92,
            status="Good",
            color="text-green-600",
            icon="layout",
            rationale="DOM structure is logical and accessible, making it easy for crawlers to index content.",
        ),
        CategoryScore(
            name="Schema",
            score=45,
            status="Poor",
            color="text-red-600",
            icon="code",
            rationale="Critical schema types for organization and breadcrumbs are missing or malformed.",
        ),
        CategoryScore(
            name="Navigation",
            score=80,
            status="Good",
            color="text-green-600",
            icon="compass",
            rationale="Site hierarchy is clear, though some deep linking paths could be optimized.",
        ),
        CategoryScore(
            name="Content Balance",
            score=70,
            status="Fair",
            color="text-yellow-600",
            icon="scale",
            rationale="Heavy reliance on images without alt text reduces textual context for AI models.",
        ),
        CategoryScore(
            name="Metadata",
            score=55,
            status="Poor",
            color="text-red-600",
            icon="file-text",
            rationale="Duplicate titles and meta descriptions found across multiple category pages.",
        ),
    ]
    recommendations: list[Recommendation] = [
        Recommendation(
            category="Schema",
            issue="Missing Product Schema markup on category pages",
            impact="High",
        ),
        Recommendation(
            category="Metadata",
            issue="Meta descriptions duplicate across 15 pages",
            impact="High",
        ),
        Recommendation(
            category="AI Optimization",
            issue="Content density too low for LLM context retrieval",
            impact="Medium",
        ),
        Recommendation(
            category="Content Balance",
            issue="Image-to-text ratio heavily skewed towards images",
            impact="Medium",
        ),
        Recommendation(
            category="Navigation",
            issue="Mobile menu depth exceeds 3 levels",
            impact="Low",
        ),
    ]

    @rx.event
    def get_progress_color(self, score: int) -> str:
        if score >= 80:
            return "bg-green-500"
        if score >= 60:
            return "bg-yellow-500"
        return "bg-red-500"