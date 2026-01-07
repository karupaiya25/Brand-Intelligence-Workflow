import reflex as rx
import asyncio
from app.states.nav_state import NavState


class Persona(rx.Base):
    id: str
    role: str
    description: str
    is_editing: bool


class Topic(rx.Base):
    id: str
    name: str
    is_editing: bool


class PersonasState(rx.State):
    active_tab: str = "personas"
    personas: list[Persona] = [
        Persona(
            id="1",
            role="The Value Seeker",
            description="Prioritizes price and durability over brand prestige.",
            is_editing=False,
        ),
        Persona(
            id="2",
            role="The Trend Hunter",
            description="Early adopter looking for the latest styles and limited releases.",
            is_editing=False,
        ),
        Persona(
            id="3",
            role="The Performance Pro",
            description="Focuses on technical specifications and competitive advantage.",
            is_editing=False,
        ),
    ]
    topics: list[Topic] = [
        Topic(id="1", name="Pricing & Value", is_editing=False),
        Topic(id="2", name="Comfort & Fit", is_editing=False),
        Topic(id="3", name="Durability", is_editing=False),
        Topic(id="4", name="Style & Aesthetics", is_editing=False),
    ]
    is_analyzing: bool = False

    @rx.event
    def set_active_tab(self, tab: str):
        self.active_tab = tab

    @rx.event
    def toggle_edit_persona(self, persona_id: str):
        updated = []
        for p in self.personas:
            if p.id == persona_id:
                p.is_editing = not p.is_editing
            updated.append(p)
        self.personas = updated

    @rx.event
    def update_persona_desc(self, persona_id: str, new_desc: str):
        updated = []
        for p in self.personas:
            if p.id == persona_id:
                p.description = new_desc
            updated.append(p)
        self.personas = updated

    @rx.event
    def toggle_edit_topic(self, topic_id: str):
        updated = []
        for t in self.topics:
            if t.id == topic_id:
                t.is_editing = not t.is_editing
            updated.append(t)
        self.topics = updated

    @rx.event
    def update_topic_name(self, topic_id: str, new_name: str):
        updated = []
        for t in self.topics:
            if t.id == topic_id:
                t.name = new_name
            updated.append(t)
        self.topics = updated

    @rx.event
    async def start_analysis(self):
        self.is_analyzing = True
        await asyncio.sleep(2.0)
        self.is_analyzing = False
        nav_state = await self.get_state(NavState)
        nav_state.set_step(3)

    @rx.var
    def generated_prompts(self) -> list[str]:
        prompts = []
        for p in self.personas:
            for t in self.topics:
                prompts.append(
                    f"Analyze {t.name} sentiments from the perspective of {p.role} who {p.description.lower().replace('.', '')}."
                )
        return prompts