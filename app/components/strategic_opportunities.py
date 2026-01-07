import reflex as rx
from app.states.strategic_opportunities_state import (
    StrategicOpportunitiesState,
    Opportunity,
)


def priority_badge(priority: str) -> rx.Component:
    return rx.el.span(
        priority,
        class_name=rx.cond(
            priority == "High",
            "px-2.5 py-0.5 rounded-full text-xs font-bold bg-red-100 text-red-700 uppercase tracking-wide",
            rx.cond(
                priority == "Medium",
                "px-2.5 py-0.5 rounded-full text-xs font-bold bg-orange-100 text-orange-700 uppercase tracking-wide",
                "px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-100 text-blue-700 uppercase tracking-wide",
            ),
        ),
    )


def action_item(text: str) -> rx.Component:
    return rx.el.li(
        rx.el.span(
            text,
            class_name="text-sm text-gray-600 group-hover:text-gray-900 transition-colors",
        ),
        class_name="flex items-start gap-2 before:content-['•'] before:text-[#fb4e0b] before:font-bold before:mr-2",
    )


def opportunity_card(opp: Opportunity) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    opp.category,
                    class_name="text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-1",
                ),
                rx.el.h3(opp.title, class_name="text-lg font-bold text-gray-900 mb-2"),
                rx.el.p(opp.description, class_name="text-sm text-gray-500 mb-4"),
                class_name="flex flex-col",
            ),
            priority_badge(opp.priority),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("user", class_name="h-3.5 w-3.5 text-gray-400 mr-1.5"),
                rx.el.span(opp.persona, class_name="text-xs font-medium text-gray-600"),
                class_name="flex items-center bg-gray-50 px-2 py-1 rounded-md",
            ),
            rx.el.div(
                rx.icon("hash", class_name="h-3.5 w-3.5 text-gray-400 mr-1.5"),
                rx.el.span(opp.topic, class_name="text-xs font-medium text-gray-600"),
                class_name="flex items-center bg-gray-50 px-2 py-1 rounded-md",
            ),
            class_name="flex flex-wrap gap-2 mb-5",
        ),
        rx.el.div(
            rx.el.h4(
                "Recommended Actions",
                class_name="text-xs font-bold text-gray-900 uppercase mb-3",
            ),
            rx.el.ul(rx.foreach(opp.action_items, action_item), class_name="space-y-2"),
            class_name="bg-gray-50/50 rounded-xl p-4 border border-gray-100",
        ),
        class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:shadow-md transition-all duration-200 group flex flex-col h-full",
    )


def filter_select(
    label: str, options: list[str], on_change: rx.event.EventType, value: str
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1.5 block",
        ),
        rx.el.div(
            rx.el.select(
                rx.foreach(options, lambda opt: rx.el.option(opt, value=opt)),
                value=value,
                on_change=on_change,
                class_name="appearance-none w-full bg-white border border-gray-200 text-gray-700 py-2.5 px-4 pr-8 rounded-xl leading-tight focus:outline-none focus:bg-white focus:border-[#fb4e0b] focus:ring-1 focus:ring-[#fb4e0b] text-sm transition-colors",
            ),
            rx.el.div(
                rx.icon("chevron-down", class_name="h-4 w-4 text-gray-400"),
                class_name="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700",
            ),
            class_name="relative",
        ),
        class_name="min-w-[180px]",
    )


def strategic_opportunities_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Strategic Opportunities",
                    class_name="text-2xl font-bold text-gray-900 mb-2",
                ),
                rx.el.p(
                    "Actionable AI-generated recommendations to improve brand performance across key segments.",
                    class_name="text-gray-500",
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                filter_select(
                    "Filter by Persona",
                    StrategicOpportunitiesState.unique_personas,
                    StrategicOpportunitiesState.set_persona_filter,
                    StrategicOpportunitiesState.selected_persona,
                ),
                filter_select(
                    "Filter by Topic",
                    StrategicOpportunitiesState.unique_topics,
                    StrategicOpportunitiesState.set_topic_filter,
                    StrategicOpportunitiesState.selected_topic,
                ),
                filter_select(
                    "Filter by Priority",
                    StrategicOpportunitiesState.unique_priorities,
                    StrategicOpportunitiesState.set_priority_filter,
                    StrategicOpportunitiesState.selected_priority,
                ),
                class_name="flex flex-wrap gap-4 mb-8 p-4 bg-white rounded-xl border border-gray-200 shadow-sm items-end",
            ),
            class_name="flex flex-col md:flex-row md:items-end md:justify-between w-full",
        ),
        rx.cond(
            StrategicOpportunitiesState.filtered_opportunities.length() > 0,
            rx.el.div(
                rx.foreach(
                    StrategicOpportunitiesState.filtered_opportunities, opportunity_card
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 animate-fade-in",
            ),
            rx.el.div(
                rx.icon("search-x", class_name="h-12 w-12 text-gray-300 mb-4"),
                rx.el.h3(
                    "No opportunities found",
                    class_name="text-lg font-medium text-gray-900 mb-1",
                ),
                rx.el.p(
                    "Try adjusting your filters to see more results.",
                    class_name="text-gray-500",
                ),
                class_name="flex flex-col items-center justify-center py-20 bg-white rounded-2xl border border-gray-200 border-dashed",
            ),
        ),
        class_name="max-w-7xl mx-auto w-full pb-10",
    )