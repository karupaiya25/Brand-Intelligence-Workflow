import reflex as rx


class Opportunity(rx.Base):
    id: str
    title: str
    description: str
    persona: str
    topic: str
    priority: str
    action_items: list[str]
    category: str


class StrategicOpportunitiesState(rx.State):
    selected_persona: str = "All"
    selected_topic: str = "All"
    selected_priority: str = "All"
    opportunities: list[Opportunity] = [
        Opportunity(
            id="1",
            title="Address Price Sensitivity",
            description="Develop a targeted campaign highlighting long-term value and durability to justify the price point.",
            persona="The Value Seeker",
            topic="Pricing & Value",
            priority="High",
            action_items=[
                "Create cost-per-wear comparison calculator",
                "Launch 'Investment Piece' email series",
                "Highlight warranty and repair services",
            ],
            category="Marketing",
        ),
        Opportunity(
            id="2",
            title="Eco-Friendly Collection Launch",
            description="Capitalize on the trend hunter's interest in sustainable fashion by launching a limited edition eco-line.",
            persona="The Trend Hunter",
            topic="Sustainability",
            priority="High",
            action_items=[
                "Partner with eco-influencers for launch",
                "Create 'Behind the Seams' content about materials",
                "Set up early access for loyal customers",
            ],
            category="Product",
        ),
        Opportunity(
            id="3",
            title="Technical Specs Deep Dive",
            description="Provide detailed technical breakdowns and lab test results on product pages.",
            persona="The Performance Pro",
            topic="Durability",
            priority="Medium",
            action_items=[
                "Add technical specification comparison table",
                "Video series featuring product engineers",
                "Update FAQ with technical Q&A",
            ],
            category="Content",
        ),
        Opportunity(
            id="4",
            title="Comfort Guarantee Program",
            description="Introduce a 30-day comfort trial to reduce purchase hesitation.",
            persona="The Value Seeker",
            topic="Comfort & Fit",
            priority="High",
            action_items=[
                "Design 'Comfort Guarantee' badge for PDPs",
                "Update return policy documentation",
                "Train support team on new policy",
            ],
            category="Service",
        ),
        Opportunity(
            id="5",
            title="Exclusive Style Drops",
            description="Create a VIP notification system for limited edition colorways.",
            persona="The Trend Hunter",
            topic="Style & Aesthetics",
            priority="Medium",
            action_items=[
                "Build SMS notification list segment",
                "Tease upcoming drops on social media",
                "Create countdown landing pages",
            ],
            category="Marketing",
        ),
        Opportunity(
            id="6",
            title="Pro-Athlete Testimonials",
            description="Leverage professional endorsements to validate performance claims.",
            persona="The Performance Pro",
            topic="Performance",
            priority="Low",
            action_items=[
                "Interview sponsored athletes",
                "Create case study blog posts",
                "Add 'Pro Choice' filter to product catalog",
            ],
            category="Social Proof",
        ),
    ]

    @rx.var
    def filtered_opportunities(self) -> list[Opportunity]:
        return [
            opp
            for opp in self.opportunities
            if (self.selected_persona == "All" or opp.persona == self.selected_persona)
            and (self.selected_topic == "All" or opp.topic == self.selected_topic)
            and (
                self.selected_priority == "All"
                or opp.priority == self.selected_priority
            )
        ]

    @rx.var
    def unique_personas(self) -> list[str]:
        return ["All"] + sorted(list(set((o.persona for o in self.opportunities))))

    @rx.var
    def unique_topics(self) -> list[str]:
        return ["All"] + sorted(list(set((o.topic for o in self.opportunities))))

    @rx.var
    def unique_priorities(self) -> list[str]:
        return ["All", "High", "Medium", "Low"]

    @rx.event
    def set_persona_filter(self, value: str):
        self.selected_persona = value

    @rx.event
    def set_topic_filter(self, value: str):
        self.selected_topic = value

    @rx.event
    def set_priority_filter(self, value: str):
        self.selected_priority = value