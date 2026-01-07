import reflex as rx
from app.states.personas_state import PersonasState, Persona, Topic


def tab_trigger(value: str, label: str, icon: str) -> rx.Component:
    is_active = PersonasState.active_tab == value
    return rx.el.button(
        rx.el.div(
            rx.icon(icon, class_name="h-4 w-4 mr-2"),
            label,
            class_name="flex items-center",
        ),
        on_click=lambda: PersonasState.set_active_tab(value),
        class_name=rx.cond(
            is_active,
            "px-6 py-3 text-sm font-medium text-[#fb4e0b] border-b-2 border-[#fb4e0b] bg-orange-50/50 transition-colors",
            "px-6 py-3 text-sm font-medium text-gray-500 hover:text-gray-700 border-b-2 border-transparent hover:border-gray-200 transition-colors",
        ),
    )


def persona_card(persona: Persona) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("user_pen", class_name="h-10 w-10 text-gray-400 mb-3"),
                rx.el.h3(persona.role, class_name="font-bold text-gray-900"),
                class_name="flex flex-col items-center text-center mb-4",
            ),
            rx.cond(
                persona.is_editing,
                rx.el.textarea(
                    default_value=persona.description,
                    on_change=lambda val: PersonasState.update_persona_desc(
                        persona.id, val
                    ),
                    class_name="w-full p-3 text-sm text-gray-600 bg-gray-50 border border-gray-200 rounded-lg focus:ring-1 focus:ring-[#fb4e0b] focus:border-[#fb4e0b] outline-none resize-none h-32",
                    auto_focus=True,
                ),
                rx.el.p(
                    persona.description,
                    class_name="text-sm text-gray-500 text-center leading-relaxed h-32 overflow-y-auto",
                ),
            ),
        ),
        rx.el.div(
            rx.el.button(
                rx.cond(persona.is_editing, "Save", "Edit"),
                on_click=lambda: PersonasState.toggle_edit_persona(persona.id),
                class_name=rx.cond(
                    persona.is_editing,
                    "text-xs font-semibold text-white bg-gray-900 px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors w-full",
                    "text-xs font-semibold text-gray-500 bg-gray-100 px-4 py-2 rounded-lg hover:bg-gray-200 transition-colors w-full",
                ),
            ),
            class_name="mt-6 pt-4 border-t border-gray-100 w-full",
        ),
        class_name="flex flex-col p-6 bg-white border border-gray-200 rounded-xl hover:shadow-md transition-shadow",
    )


def topic_item(topic: Topic) -> rx.Component:
    return rx.el.div(
        rx.cond(
            topic.is_editing,
            rx.el.input(
                default_value=topic.name,
                on_change=lambda val: PersonasState.update_topic_name(topic.id, val),
                class_name="flex-1 px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-1 focus:ring-[#fb4e0b] focus:border-[#fb4e0b] outline-none",
                auto_focus=True,
            ),
            rx.el.div(
                rx.icon("hash", class_name="h-4 w-4 text-[#fb4e0b] mr-3"),
                rx.el.span(topic.name, class_name="text-sm font-medium text-gray-700"),
                class_name="flex items-center flex-1",
            ),
        ),
        rx.el.button(
            rx.icon(rx.cond(topic.is_editing, "check", "pencil"), class_name="h-4 w-4"),
            on_click=lambda: PersonasState.toggle_edit_topic(topic.id),
            class_name="ml-4 p-2 text-gray-400 hover:text-[#fb4e0b] hover:bg-orange-50 rounded-lg transition-colors",
        ),
        class_name="flex items-center justify-between p-4 bg-white border border-gray-200 rounded-xl hover:border-gray-300 transition-colors",
    )


def prompt_item(prompt: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                "sparkles",
                class_name="h-5 w-5 text-[#fb4e0b] mt-0.5 mr-3 flex-shrink-0",
            ),
            rx.el.p(prompt, class_name="text-sm text-gray-600 leading-relaxed"),
            class_name="flex items-start",
        ),
        class_name="p-4 bg-gray-50 border border-gray-100 rounded-xl",
    )


def personas_setup_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Personas & Topics",
                    class_name="text-2xl font-bold text-gray-900 mb-2",
                ),
                rx.el.p(
                    "Review the AI-generated personas and analysis topics. You can edit them to better align with your strategic goals.",
                    class_name="text-gray-500",
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    tab_trigger("personas", "Consumer Personas", "users"),
                    tab_trigger("topics", "Analysis Topics", "message-square"),
                    tab_trigger("prompts", "Generated Prompts", "square_terminal"),
                    class_name="flex border-b border-gray-200 w-full overflow-x-auto",
                ),
                class_name="mb-8",
            ),
            rx.el.div(
                rx.cond(
                    PersonasState.active_tab == "personas",
                    rx.el.div(
                        rx.foreach(PersonasState.personas, persona_card),
                        class_name="grid grid-cols-1 md:grid-cols-3 gap-6 animate-fade-in",
                    ),
                ),
                rx.cond(
                    PersonasState.active_tab == "topics",
                    rx.el.div(
                        rx.foreach(PersonasState.topics, topic_item),
                        class_name="grid grid-cols-1 md:grid-cols-2 gap-4 animate-fade-in",
                    ),
                ),
                rx.cond(
                    PersonasState.active_tab == "prompts",
                    rx.el.div(
                        rx.el.p(
                            "These are the analysis prompts that will be sent to the AI engine based on your personas and topics.",
                            class_name="text-sm text-gray-500 mb-6",
                        ),
                        rx.el.div(
                            rx.foreach(PersonasState.generated_prompts, prompt_item),
                            class_name="space-y-3 max-h-[500px] overflow-y-auto pr-2 custom-scrollbar",
                        ),
                        class_name="animate-fade-in",
                    ),
                ),
                class_name="min-h-[400px]",
            ),
            rx.el.div(class_name="h-px bg-gray-100 w-full my-8"),
            rx.el.div(
                rx.el.div(
                    rx.icon("check_check", class_name="text-green-500 h-5 w-5 mr-2"),
                    rx.el.span(
                        "Configuration ready for deep analysis",
                        class_name="text-sm text-gray-500",
                    ),
                    class_name="flex items-center",
                ),
                rx.el.button(
                    rx.cond(
                        PersonasState.is_analyzing,
                        rx.el.div(
                            rx.spinner(size="2", class_name="mr-2 text-white"),
                            "Analyzing Data...",
                            class_name="flex items-center",
                        ),
                        "Run Full Analysis",
                    ),
                    on_click=PersonasState.start_analysis,
                    disabled=PersonasState.is_analyzing,
                    class_name="bg-[#fb4e0b] text-white px-8 py-3 rounded-xl font-semibold hover:bg-[#e04309] transition-all shadow-lg shadow-orange-500/20 hover:shadow-orange-500/30 disabled:opacity-70 disabled:cursor-not-allowed",
                ),
                class_name="flex items-center justify-between mt-auto",
            ),
            class_name="flex flex-col",
        ),
        class_name="max-w-6xl mx-auto w-full bg-white p-8 rounded-2xl border border-gray-200 shadow-sm",
    )