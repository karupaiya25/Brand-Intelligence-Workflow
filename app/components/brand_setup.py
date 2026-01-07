import reflex as rx
from app.states.brand_state import BrandState


def form_field(
    label: str,
    placeholder: str,
    value: str,
    on_change: rx.event.EventType,
    is_text_area: bool = False,
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-semibold text-gray-700 mb-2"),
        rx.cond(
            is_text_area,
            rx.el.textarea(
                placeholder=placeholder,
                on_change=on_change,
                rows=4,
                class_name="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#fb4e0b] focus:ring-1 focus:ring-[#fb4e0b] outline-none transition-all duration-200 bg-white text-gray-800 text-sm resize-none placeholder:text-gray-400",
                default_value=value,
            ),
            rx.el.input(
                placeholder=placeholder,
                on_change=on_change,
                class_name="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#fb4e0b] focus:ring-1 focus:ring-[#fb4e0b] outline-none transition-all duration-200 bg-white text-gray-800 text-sm placeholder:text-gray-400",
                default_value=value,
            ),
        ),
        class_name="mb-5",
    )


def brand_setup_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Brand Configuration",
                class_name="text-2xl font-bold text-gray-900 mb-2",
            ),
            rx.el.p(
                "Enter your brand details below. We can try to auto-fill information based on your brand name.",
                class_name="text-gray-500 mb-8",
            ),
            class_name="mb-2",
        ),
        rx.el.div(
            rx.cond(
                BrandState.is_loading,
                rx.el.div(
                    rx.el.div(
                        rx.spinner(size="3", class_name="text-[#fb4e0b] mb-4"),
                        rx.el.p(
                            "Analyzing brand details...",
                            class_name="text-[#fb4e0b] font-medium animate-pulse",
                        ),
                        class_name="flex flex-col items-center justify-center h-full w-full absolute inset-0 bg-white/80 backdrop-blur-sm z-10 rounded-2xl",
                    )
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Brand Name",
                        class_name="block text-sm font-semibold text-gray-700 mb-2",
                    ),
                    rx.el.div(
                        rx.el.input(
                            placeholder="e.g. Nike, Apple, Coca-Cola",
                            on_change=BrandState.set_brand_name,
                            class_name="flex-1 px-4 py-3 rounded-xl border border-gray-200 focus:border-[#fb4e0b] focus:ring-1 focus:ring-[#fb4e0b] outline-none transition-all duration-200 bg-white text-gray-800 text-sm",
                            default_value=BrandState.brand_name,
                        ),
                        rx.el.button(
                            rx.cond(
                                BrandState.is_loading,
                                "Scanning...",
                                "Auto-fill Details",
                            ),
                            on_click=BrandState.auto_fill_brand_info,
                            disabled=BrandState.brand_name == "",
                            class_name="px-6 py-3 bg-gray-900 text-white font-medium rounded-xl hover:bg-gray-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed whitespace-nowrap text-sm shadow-sm hover:shadow-md",
                        ),
                        class_name="flex gap-3",
                    ),
                    class_name="mb-8",
                ),
                rx.el.div(class_name="h-px bg-gray-100 w-full mb-8"),
                rx.el.div(
                    rx.el.div(
                        form_field(
                            "Official Title",
                            "Brand tagline or official title",
                            BrandState.brand_title,
                            BrandState.set_brand_title,
                        ),
                        form_field(
                            "Website URL",
                            "https://example.com",
                            BrandState.brand_url,
                            BrandState.set_brand_url,
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                    ),
                    form_field(
                        "Brand Summary",
                        "A brief description of what the brand stands for...",
                        BrandState.brand_summary,
                        BrandState.set_brand_summary,
                        is_text_area=True,
                    ),
                    class_name="animate-fade-in",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "check_check", class_name="text-green-500 h-5 w-5 mr-2"
                        ),
                        rx.el.span(
                            "Review the details before proceeding",
                            class_name="text-sm text-gray-500",
                        ),
                        class_name="flex items-center",
                    ),
                    rx.el.button(
                        "Confirm & Setup Brand",
                        on_click=BrandState.complete_setup,
                        class_name="bg-[#fb4e0b] text-white px-8 py-3 rounded-xl font-semibold hover:bg-[#e04309] transition-all shadow-lg shadow-orange-500/20 hover:shadow-orange-500/30 flex items-center gap-2",
                    ),
                    class_name="flex items-center justify-between mt-8 pt-6 border-t border-gray-100",
                ),
                class_name="relative",
            ),
            class_name="bg-white p-8 rounded-2xl border border-gray-200 shadow-sm relative overflow-hidden",
        ),
        class_name="max-w-4xl mx-auto w-full",
    )