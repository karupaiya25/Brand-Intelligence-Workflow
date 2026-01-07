import reflex as rx
from app.states.insights_state import InsightsState


def card_wrapper(
    title: str, content: rx.Component, col_span: str = "col-span-1"
) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-lg font-bold text-gray-900 mb-4"),
        content,
        class_name=f"bg-white p-6 rounded-2xl border border-gray-200 shadow-sm {col_span} hover:shadow-md transition-shadow",
    )


def competitive_chart() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Rank",
                            class_name="text-left py-2 text-gray-500 font-semibold",
                        ),
                        rx.el.th(
                            "Brand",
                            class_name="text-left py-2 text-gray-500 font-semibold",
                        ),
                        rx.el.th(
                            "Mentions",
                            class_name="text-right py-2 text-gray-500 font-semibold",
                        ),
                    ),
                    class_name="text-xs border-b border-gray-100",
                ),
                rx.el.tbody(
                    rx.foreach(
                        InsightsState.competitive_data,
                        lambda item: rx.el.tr(
                            rx.el.td(
                                rx.el.span(
                                    f"#{item['rank']}",
                                    class_name=rx.cond(
                                        item["rank"] == 1,
                                        "bg-[#fb4e0b] text-white px-2 py-0.5 rounded-full text-[10px]",
                                        "text-gray-500",
                                    ),
                                ),
                                class_name="py-3",
                            ),
                            rx.el.td(
                                item["name"],
                                class_name="py-3 font-medium text-gray-900",
                            ),
                            rx.el.td(
                                item["mentions"],
                                class_name="py-3 text-right text-gray-600",
                            ),
                            class_name="border-b border-gray-50 last:border-0",
                        ),
                    )
                ),
                class_name="w-full",
            ),
            class_name="mb-4",
        ),
        rx.recharts.bar_chart(
            rx.recharts.cartesian_grid(stroke_dasharray="3 3", vertical=False),
            rx.recharts.graphing_tooltip(cursor=False, wrapper_style={"zIndex": 1000}),
            rx.recharts.x_axis(
                data_key="name",
                axis_line=False,
                tick_line=False,
                font_size=10,
                hide=True,
            ),
            rx.recharts.y_axis(axis_line=False, tick_line=False, font_size=10),
            rx.recharts.bar(
                data_key="mentions", fill="#fb4e0b", radius=[4, 4, 0, 0], bar_size=40
            ),
            data=InsightsState.competitive_data,
            width="100%",
            height=150,
            class_name="text-xs",
        ),
        class_name="flex flex-col h-full",
    )


def persona_trend_chart() -> rx.Component:
    return rx.recharts.area_chart(
        rx.recharts.cartesian_grid(stroke_dasharray="3 3", vertical=False),
        rx.recharts.graphing_tooltip(wrapper_style={"zIndex": 1000}),
        rx.recharts.x_axis(
            data_key="month", axis_line=False, tick_line=False, font_size=10
        ),
        rx.recharts.y_axis(axis_line=False, tick_line=False, font_size=10),
        rx.recharts.area(
            type_="monotone",
            data_key="Value Seeker",
            stack_id="1",
            stroke="#fb4e0b",
            fill="#fb4e0b",
            fill_opacity=0.6,
        ),
        rx.recharts.area(
            type_="monotone",
            data_key="Trend Hunter",
            stack_id="1",
            stroke="#005071",
            fill="#005071",
            fill_opacity=0.6,
        ),
        rx.recharts.area(
            type_="monotone",
            data_key="Performance Pro",
            stack_id="1",
            stroke="#ababab",
            fill="#ababab",
            fill_opacity=0.6,
        ),
        data=InsightsState.persona_visibility_data,
        width="100%",
        height=250,
        class_name="text-xs",
    )


def topic_chart() -> rx.Component:
    return rx.recharts.bar_chart(
        rx.recharts.cartesian_grid(stroke_dasharray="3 3", horizontal=False),
        rx.recharts.graphing_tooltip(cursor=False, wrapper_style={"zIndex": 1000}),
        rx.recharts.x_axis(type_="number", hide=True),
        rx.recharts.y_axis(
            data_key="topic",
            type_="category",
            width=100,
            axis_line=False,
            tick_line=False,
            font_size=11,
        ),
        rx.recharts.bar(
            data_key="count", fill="#005071", radius=[0, 4, 4, 0], bar_size=20
        ),
        layout="vertical",
        data=InsightsState.topic_data,
        width="100%",
        height=250,
        class_name="text-xs",
    )


def sources_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h4(
            "Top Domains",
            class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4 text-center",
        ),
        rx.recharts.pie_chart(
            rx.recharts.graphing_tooltip(wrapper_style={"zIndex": 1000}),
            rx.recharts.pie(
                data=InsightsState.source_data,
                data_key="value",
                name_key="name",
                cx="50%",
                cy="50%",
                inner_radius=40,
                outer_radius=60,
                padding_angle=2,
                stroke="#fff",
                stroke_width=1,
            ),
            width="100%",
            height=150,
        ),
        rx.el.div(
            rx.foreach(
                InsightsState.source_data,
                lambda item: rx.el.div(
                    rx.el.div(
                        class_name="w-2 h-2 rounded-full mr-2",
                        style={"background_color": item["fill"]},
                    ),
                    rx.el.span(
                        item["name"],
                        class_name="text-xs text-gray-600 truncate max-w-[100px]",
                    ),
                    class_name="flex items-center mb-1",
                ),
            ),
            class_name="flex flex-col gap-1 mt-2 w-full px-4",
        ),
        class_name="flex flex-col items-center",
    )


def consumer_attributes_chart() -> rx.Component:
    return rx.el.div(
        rx.foreach(
            InsightsState.consumer_attributes,
            lambda item: rx.el.div(
                rx.el.div(
                    rx.el.span(
                        item["attribute"],
                        class_name="text-xs font-medium text-gray-700",
                    ),
                    rx.el.span(
                        f"{item['weight']}%",
                        class_name="text-xs font-bold text-[#fb4e0b]",
                    ),
                    class_name="flex justify-between mb-1",
                ),
                rx.el.div(
                    rx.el.div(
                        class_name="h-full rounded-full",
                        style={
                            "width": f"{item['weight']}%",
                            "background_color": item["fill"],
                        },
                    ),
                    class_name="w-full h-1.5 bg-gray-100 rounded-full overflow-hidden",
                ),
                class_name="mb-3 last:mb-0",
            ),
        ),
        class_name="flex flex-col justify-center h-full py-2",
    )


def sentiment_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span("Overall Score", class_name="text-sm text-gray-500"),
            rx.el.span(
                f"{InsightsState.sentiment_score}/100",
                class_name="text-3xl font-bold text-[#fb4e0b]",
            ),
            class_name="flex flex-col items-center mb-6",
        ),
        rx.el.div(
            rx.foreach(
                InsightsState.sentiment_distribution,
                lambda item: rx.el.div(
                    rx.el.div(
                        rx.el.span(item["type"], class_name="text-xs font-medium w-16"),
                        rx.el.div(
                            rx.el.div(
                                class_name=f"h-full rounded-full {item['color']}",
                                style={"width": f"{item['value']}%%"},
                            ),
                            class_name="flex-1 h-2 bg-gray-100 rounded-full mx-3",
                        ),
                        rx.el.span(
                            f"{item['value']}%%",
                            class_name="text-xs text-gray-500 w-8 text-right",
                        ),
                        class_name="flex items-center w-full",
                    ),
                    class_name="mb-3 last:mb-0",
                ),
            ),
            class_name="w-full space-y-2",
        ),
        class_name="flex flex-col h-full justify-center",
    )


def heatmap_row(item: dict) -> rx.Component:
    def cell(val: rx.Var) -> rx.Component:
        val_int = val.to(int)
        return rx.el.div(
            rx.el.span(
                val, class_name="text-xs font-medium text-gray-700 z-10 relative"
            ),
            class_name=rx.cond(
                val_int > 80,
                "h-12 flex items-center justify-center rounded bg-[#fb4e0b]/40 relative",
                rx.cond(
                    val_int > 60,
                    "h-12 flex items-center justify-center rounded bg-[#fb4e0b]/25 relative",
                    rx.cond(
                        val_int > 40,
                        "h-12 flex items-center justify-center rounded bg-[#fb4e0b]/10 relative",
                        "h-12 flex items-center justify-center rounded bg-gray-50 relative",
                    ),
                ),
            ),
        )

    return rx.el.div(
        rx.el.div(
            item["label"],
            class_name="text-xs font-medium text-gray-600 flex items-center",
        ),
        cell(item["c1"]),
        cell(item["c2"]),
        cell(item["c3"]),
        class_name="grid grid-cols-4 gap-2 mb-2",
    )


def heatmap_matrix(data: list[dict]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div("", class_name=""),
            rx.foreach(
                InsightsState.competitor_names,
                lambda name: rx.el.div(
                    name,
                    class_name="text-xs font-bold text-gray-400 text-center uppercase tracking-wider",
                ),
            ),
            class_name="grid grid-cols-4 gap-2 mb-2",
        ),
        rx.foreach(data, heatmap_row),
        class_name="w-full",
    )


def word_cloud() -> rx.Component:
    return rx.el.div(
        rx.el.h4(
            "Top 10 Associations",
            class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4 absolute top-0 left-0",
        ),
        rx.foreach(
            InsightsState.word_cloud,
            lambda word: rx.el.span(
                word["text"],
                class_name=f"{word['size']} {word['color']} font-bold opacity-80 hover:opacity-100 transition-opacity cursor-default",
            ),
        ),
        class_name="flex flex-wrap gap-x-4 gap-y-3 items-center justify-center content-center h-full p-6 relative",
    )


def insights_dashboard() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Insights Dashboard", class_name="text-2xl font-bold text-gray-900"
            ),
            rx.el.p(
                "AI-driven analysis of your brand performance across market segments.",
                class_name="text-gray-500",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            card_wrapper(
                "Competitive Benchmarking", competitive_chart(), "md:col-span-2"
            ),
            card_wrapper(
                "Persona Engagement Trend", persona_trend_chart(), "md:col-span-2"
            ),
            card_wrapper("Sentiment Analysis", sentiment_section(), "md:col-span-1"),
            card_wrapper(
                "Consumer Attributes", consumer_attributes_chart(), "md:col-span-1"
            ),
            card_wrapper("Topic Visibility", topic_chart(), "md:col-span-2"),
            card_wrapper(
                "Persona vs Competitor Affinity",
                heatmap_matrix(InsightsState.heatmap_data),
                "md:col-span-2",
            ),
            card_wrapper(
                "Topic vs Competitor Matrix",
                heatmap_matrix(InsightsState.topic_matrix_data),
                "md:col-span-2",
            ),
            card_wrapper("Top Sources", sources_chart(), "md:col-span-1"),
            card_wrapper("Brand Associations Map", word_cloud(), "md:col-span-3"),
            class_name="grid grid-cols-1 md:grid-cols-4 gap-6",
        ),
        class_name="max-w-7xl mx-auto w-full pb-10",
    )