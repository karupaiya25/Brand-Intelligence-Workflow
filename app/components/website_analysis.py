import reflex as rx
from app.states.website_analysis_state import (
    WebsiteAnalysisState,
    CategoryScore,
    Recommendation,
)


def score_badge(score: int) -> rx.Component:
    return rx.el.div(
        rx.el.span(f"{score}/100", class_name="text-xs font-bold text-white"),
        class_name=rx.cond(
            score >= 80,
            "px-2 py-1 rounded-full bg-green-500",
            rx.cond(
                score >= 60,
                "px-2 py-1 rounded-full bg-yellow-500",
                "px-2 py-1 rounded-full bg-red-500",
            ),
        ),
    )


def category_card(category: CategoryScore) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(category.icon, class_name=f"h-6 w-6 {category.color} mb-3"),
                rx.el.div(
                    rx.el.h4(category.name, class_name="font-semibold text-gray-900"),
                    rx.el.span(
                        category.status,
                        class_name=f"text-xs font-medium {category.color}",
                    ),
                    class_name="flex flex-col",
                ),
                class_name="flex flex-col items-start",
            ),
            score_badge(category.score),
            class_name="flex justify-between items-start mb-2",
        ),
        rx.el.div(
            rx.el.p(
                category.rationale,
                class_name="text-xs text-gray-500 italic mb-4 leading-relaxed bg-gray-50 p-2 rounded-lg border border-gray-100",
            ),
            class_name="mb-2",
        ),
        rx.el.div(
            rx.el.div(
                class_name=rx.cond(
                    category.score >= 80,
                    "h-full rounded-full bg-green-500",
                    rx.cond(
                        category.score >= 60,
                        "h-full rounded-full bg-yellow-500",
                        "h-full rounded-full bg-red-500",
                    ),
                ),
                style={"width": f"{category.score}%%"},
            ),
            class_name="w-full h-2 bg-gray-100 rounded-full overflow-hidden",
        ),
        class_name="bg-white p-5 rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-shadow",
    )


def recommendation_row(rec: Recommendation) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                rec.impact,
                class_name=rx.cond(
                    rec.impact == "High",
                    "px-2 py-0.5 rounded text-[10px] font-bold bg-red-100 text-red-700 uppercase tracking-wide",
                    rx.cond(
                        rec.impact == "Medium",
                        "px-2 py-0.5 rounded text-[10px] font-bold bg-yellow-100 text-yellow-700 uppercase tracking-wide",
                        "px-2 py-0.5 rounded text-[10px] font-bold bg-blue-100 text-blue-700 uppercase tracking-wide",
                    ),
                ),
            ),
            rx.el.h5(
                rec.category, class_name="text-sm font-semibold text-gray-900 ml-3"
            ),
            class_name="flex items-center mb-1",
        ),
        rx.el.p(rec.issue, class_name="text-sm text-gray-600 ml-[calc(2rem+0.75rem)]"),
        class_name="p-4 border-b border-gray-50 last:border-0 hover:bg-gray-50 transition-colors",
    )


def website_analysis_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Website Analysis", class_name="text-2xl font-bold text-gray-900 mb-2"
            ),
            rx.el.p(
                "Technical and content audit to optimize for AI search engines.",
                class_name="text-gray-500",
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Site Health", class_name="text-lg font-bold text-gray-900 mb-6"
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            WebsiteAnalysisState.overall_health_score,
                            class_name="text-6xl font-bold text-[#fb4e0b]",
                        ),
                        rx.el.span(
                            "of 100", class_name="text-gray-400 font-medium mt-2"
                        ),
                        class_name="flex flex-col items-center justify-center w-48 h-48 rounded-full border-8 border-orange-100 bg-white shadow-sm mx-auto",
                    ),
                    rx.el.p(
                        "Your website structure is generally good, but lacks specific semantic markup required for optimal LLM parsing.",
                        class_name="text-center text-gray-500 text-sm mt-6 max-w-xs mx-auto",
                    ),
                    class_name="flex flex-col",
                ),
                class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm lg:col-span-1",
            ),
            rx.el.div(
                rx.foreach(WebsiteAnalysisState.categories, category_card),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 lg:col-span-3",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-4 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Prioritized Recommendations",
                    class_name="text-lg font-bold text-gray-900",
                ),
                rx.el.button(
                    "Download Report",
                    class_name="text-sm font-medium text-[#fb4e0b] hover:underline",
                ),
                class_name="flex justify-between items-center mb-4 px-2",
            ),
            rx.el.div(
                rx.foreach(WebsiteAnalysisState.recommendations, recommendation_row),
                class_name="bg-white rounded-2xl border border-gray-200 shadow-sm overflow-hidden",
            ),
            class_name="w-full",
        ),
        class_name="max-w-7xl mx-auto w-full pb-10",
    )