import reflex as rx
from app.states.nav_state import NavState


def nav_item(item: dict, index: int) -> rx.Component:
    is_active = NavState.current_step_index == index
    active_bg = "bg-[#fb4e0b]"
    active_text = "text-white"
    active_border = "border-r-4 border-white"
    inactive_text = "text-gray-400 hover:bg-gray-700 hover:text-white"
    inactive_border = "border-r-4 border-transparent"
    return rx.el.button(
        rx.el.div(
            rx.icon(
                item["icon"],
                class_name=rx.cond(
                    is_active,
                    "h-5 w-5 mr-3 text-white",
                    "h-5 w-5 mr-3 text-gray-400 group-hover:text-white",
                ),
            ),
            rx.el.span(item["label"], class_name="font-medium text-sm"),
            class_name="flex items-center w-full",
        ),
        on_click=lambda: NavState.set_step(index),
        class_name=rx.cond(
            is_active,
            f"w-full p-3 pl-4 flex items-center transition-all duration-200 rounded-r-lg mr-2 {active_bg} {active_text}",
            f"w-full p-3 pl-4 flex items-center transition-all duration-200 rounded-r-lg mr-2 group {inactive_text}",
        ),
    )


def sidebar_section(title: str, items: list[dict], offset: int = 0) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            title,
            class_name="px-4 text-xs font-bold text-gray-500 uppercase tracking-wider mb-2 mt-2",
        ),
        rx.el.div(
            rx.foreach(items, lambda item, i: nav_item(item, i + offset)),
            class_name="flex flex-col gap-1",
        ),
        class_name="mb-6",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon("bar-chart-2", class_name="h-8 w-8 text-[#fb4e0b] mr-2"),
                rx.el.h1(
                    "BrandAI", class_name="text-xl font-bold text-white tracking-tight"
                ),
                class_name="flex items-center mb-2",
            ),
            rx.el.p(
                "Analytics Platform",
                class_name="text-xs text-gray-400 font-medium pl-10",
            ),
            class_name="p-6 border-b border-gray-700",
        ),
        rx.el.nav(
            sidebar_section("Configuration", NavState.configuration_steps, offset=0),
            sidebar_section("Analytics", NavState.analytics_steps, offset=3),
            class_name="flex flex-col py-6 overflow-y-auto flex-1",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("user", class_name="h-5 w-5 text-gray-300"),
                    class_name="h-8 w-8 rounded-full bg-gray-600 flex items-center justify-center mr-3",
                ),
                rx.el.div(
                    rx.el.p("Admin User", class_name="text-sm font-medium text-white"),
                    rx.el.p("admin@exl.com", class_name="text-xs text-gray-400"),
                    class_name="flex flex-col",
                ),
                class_name="flex items-center p-2 rounded-lg hover:bg-gray-700 transition-colors cursor-pointer",
            ),
            class_name="p-4 border-t border-gray-700 bg-[#424242]",
        ),
        class_name="flex flex-col w-72 h-screen bg-[#424242] border-r border-gray-700 fixed left-0 top-0 z-30",
    )