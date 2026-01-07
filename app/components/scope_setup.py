import reflex as rx
from app.states.scope_state import ScopeState, Product


def scope_option_card(
    value: str, title: str, description: str, icon_name: str
) -> rx.Component:
    is_selected = ScopeState.scope_type == value
    return rx.el.button(
        rx.el.div(
            rx.icon(
                icon_name,
                class_name=rx.cond(
                    is_selected,
                    "h-8 w-8 text-[#fb4e0b] mb-4",
                    "h-8 w-8 text-gray-400 mb-4 group-hover:text-gray-600",
                ),
            ),
            rx.el.h3(
                title,
                class_name=rx.cond(
                    is_selected,
                    "text-lg font-bold text-[#fb4e0b] mb-2",
                    "text-lg font-bold text-gray-900 mb-2",
                ),
            ),
            rx.el.p(
                description,
                class_name="text-sm text-gray-500 text-left leading-relaxed",
            ),
            class_name="flex flex-col items-start h-full",
        ),
        on_click=lambda: ScopeState.set_scope_type(value),
        class_name=rx.cond(
            is_selected,
            "flex-1 p-6 rounded-2xl border-2 border-[#fb4e0b] bg-[#fb4e0b]/5 text-left transition-all duration-200 relative overflow-hidden",
            "flex-1 p-6 rounded-2xl border border-gray-200 bg-white text-left hover:border-gray-300 hover:shadow-sm transition-all duration-200 group",
        ),
    )


def product_row(product: Product) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            rx.el.input(
                type="checkbox",
                checked=product.selected,
                on_change=lambda _: ScopeState.toggle_product(product.id),
                class_name="w-5 h-5 text-[#fb4e0b] border-gray-300 rounded focus:ring-[#fb4e0b] mr-4 cursor-pointer",
            ),
            rx.el.div(
                rx.el.p(product.name, class_name="font-medium text-gray-900"),
                rx.el.p(product.category, class_name="text-xs text-gray-500"),
                class_name="flex flex-col",
            ),
            class_name="flex items-center cursor-pointer w-full",
        ),
        class_name="p-3 hover:bg-gray-50 rounded-lg transition-colors",
    )


def scope_setup_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Analysis Scope", class_name="text-2xl font-bold text-gray-900 mb-2"
            ),
            rx.el.p(
                "Determine the breadth of your brand analysis. You can focus on the brand level or dive deep into specific product lines.",
                class_name="text-gray-500 mb-8",
            ),
            class_name="mb-2",
        ),
        rx.el.div(
            rx.el.div(
                scope_option_card(
                    "brand",
                    "Brand Only",
                    "Analyze general brand sentiment, market positioning, and high-level themes without specific product breakdown.",
                    "building-2",
                ),
                scope_option_card(
                    "all_products",
                    "All Products",
                    "Include a comprehensive analysis of all detected products associated with your brand.",
                    "package",
                ),
                scope_option_card(
                    "specific_products",
                    "Specific Products",
                    "Select specific key products or categories to focus the analysis on.",
                    "list-checks",
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8",
            ),
            rx.cond(
                ScopeState.scope_type == "specific_products",
                rx.el.div(
                    rx.el.div(
                        rx.el.h4(
                            "Select Products to Analyze",
                            class_name="font-semibold text-gray-900 mb-4",
                        ),
                        rx.el.div(
                            rx.foreach(ScopeState.products, product_row),
                            class_name="grid grid-cols-1 md:grid-cols-2 gap-2 max-h-60 overflow-y-auto p-1",
                        ),
                        class_name="bg-gray-50 p-6 rounded-xl border border-gray-100 mb-8 animate-fade-in",
                    )
                ),
            ),
            rx.el.div(class_name="h-px bg-gray-100 w-full mb-8"),
            rx.el.div(
                rx.el.div(
                    rx.icon("info", class_name="text-blue-500 h-5 w-5 mr-2"),
                    rx.el.span(
                        "AI analysis will take approximately 1-2 minutes",
                        class_name="text-sm text-gray-500",
                    ),
                    class_name="flex items-center",
                ),
                rx.el.button(
                    rx.cond(
                        ScopeState.is_analyzing,
                        rx.el.div(
                            rx.spinner(size="2", class_name="mr-2 text-white"),
                            "Processing...",
                            class_name="flex items-center",
                        ),
                        "Generate Personas & Topics",
                    ),
                    on_click=ScopeState.analyze_scope,
                    disabled=ScopeState.is_analyzing,
                    class_name="bg-[#fb4e0b] text-white px-8 py-3 rounded-xl font-semibold hover:bg-[#e04309] transition-all shadow-lg shadow-orange-500/20 hover:shadow-orange-500/30 disabled:opacity-70 disabled:cursor-not-allowed",
                ),
                class_name="flex items-center justify-between mt-auto pt-2",
            ),
            class_name="flex flex-col",
        ),
        class_name="max-w-5xl mx-auto w-full bg-white p-8 rounded-2xl border border-gray-200 shadow-sm",
    )