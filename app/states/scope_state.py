import reflex as rx
import asyncio
from app.states.nav_state import NavState


class Product(rx.Base):
    id: str
    name: str
    category: str
    selected: bool


class ScopeState(rx.State):
    scope_type: str = "brand"
    products: list[Product] = [
        Product(id="p1", name="Air Zoom Pegasus", category="Running", selected=False),
        Product(id="p2", name="Dri-FIT Tee", category="Apparel", selected=False),
        Product(id="p3", name="Air Force 1", category="Lifestyle", selected=False),
        Product(id="p4", name="Pro Hijab", category="Accessories", selected=False),
        Product(id="p5", name="Metcon 8", category="Training", selected=False),
    ]
    is_analyzing: bool = False

    @rx.event
    def set_scope_type(self, value: str):
        self.scope_type = value

    @rx.event
    def toggle_product(self, product_id: str):
        updated_products = []
        for p in self.products:
            if p.id == product_id:
                p.selected = not p.selected
            updated_products.append(p)
        self.products = updated_products

    @rx.event
    async def analyze_scope(self):
        self.is_analyzing = True
        await asyncio.sleep(1.5)
        self.is_analyzing = False
        nav_state = await self.get_state(NavState)
        nav_state.set_step(2)