import reflex as rx


class NavState(rx.State):
    current_step_index: int = 0
    steps: list[dict[str, str]] = [
        {
            "id": "brand_setup",
            "label": "Brand Setup",
            "icon": "building-2",
            "category": "Configuration",
        },
        {
            "id": "scope_setup",
            "label": "Scope Setup",
            "icon": "target",
            "category": "Configuration",
        },
        {
            "id": "personas",
            "label": "Personas & Topics",
            "icon": "users",
            "category": "Configuration",
        },
        {
            "id": "insights",
            "label": "Insights Dashboard",
            "icon": "bar-chart-3",
            "category": "Analytics",
        },
        {
            "id": "website",
            "label": "Website Analysis",
            "icon": "globe",
            "category": "Analytics",
        },
        {
            "id": "strategy",
            "label": "Strategic Opportunities",
            "icon": "lightbulb",
            "category": "Analytics",
        },
    ]

    @rx.var
    def configuration_steps(self) -> list[dict[str, str]]:
        return [s for s in self.steps if s["category"] == "Configuration"]

    @rx.var
    def analytics_steps(self) -> list[dict[str, str]]:
        return [s for s in self.steps if s["category"] == "Analytics"]

    @rx.event
    def set_step(self, index: int):
        self.current_step_index = index

    @rx.event
    def next_step(self):
        if self.current_step_index < len(self.steps) - 1:
            self.current_step_index += 1

    @rx.event
    def prev_step(self):
        if self.current_step_index > 0:
            self.current_step_index -= 1