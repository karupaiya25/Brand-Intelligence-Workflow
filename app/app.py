import reflex as rx
from app.components.sidebar import sidebar
from app.components.brand_setup import brand_setup_card
from app.states.nav_state import NavState
from app.components.scope_setup import scope_setup_card
from app.components.personas_setup import personas_setup_card
from app.components.insights_dashboard import insights_dashboard
from app.components.website_analysis import website_analysis_card
from app.components.strategic_opportunities import strategic_opportunities_view


def content_area() -> rx.Component:
    return rx.el.div(
        rx.cond(
            NavState.current_step_index == 0,
            brand_setup_card(),
            rx.cond(
                NavState.current_step_index == 1,
                scope_setup_card(),
                rx.cond(
                    NavState.current_step_index == 2,
                    personas_setup_card(),
                    rx.cond(
                        NavState.current_step_index == 3,
                        insights_dashboard(),
                        rx.cond(
                            NavState.current_step_index == 4,
                            website_analysis_card(),
                            rx.cond(
                                NavState.current_step_index == 5,
                                strategic_opportunities_view(),
                                rx.el.div(
                                    rx.el.h2(
                                        "Unknown Step",
                                        class_name="text-2xl font-bold text-gray-900",
                                    ),
                                    rx.el.p(
                                        "This page does not exist.",
                                        class_name="text-gray-500 mt-2",
                                    ),
                                    class_name="max-w-4xl mx-auto w-full bg-white p-8 rounded-2xl border border-gray-200 shadow-sm",
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        class_name="flex-1 min-h-screen ml-72 p-8 bg-[#f8f9fa]",
    )


def index() -> rx.Component:
    return rx.el.div(
        sidebar(),
        content_area(),
        class_name="flex min-h-screen bg-[#f8f9fa] font-['Inter']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
    ],
)
app.add_page(index, route="/")