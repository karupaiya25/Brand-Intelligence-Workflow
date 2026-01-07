import reflex as rx
import asyncio
from app.states.nav_state import NavState


class BrandState(rx.State):
    brand_name: str = ""
    brand_title: str = ""
    brand_url: str = ""
    brand_summary: str = ""
    is_loading: bool = False
    is_setup_complete: bool = False

    @rx.event
    def set_brand_name(self, value: str):
        self.brand_name = value

    @rx.event
    def set_brand_title(self, value: str):
        self.brand_title = value

    @rx.event
    def set_brand_url(self, value: str):
        self.brand_url = value

    @rx.event
    def set_brand_summary(self, value: str):
        self.brand_summary = value

    @rx.event(background=True)
    async def auto_fill_brand_info(self):
        async with self:
            if not self.brand_name:
                return
            self.is_loading = True
        await asyncio.sleep(1.5)
        async with self:
            name = self.brand_name.lower()
            if "nike" in name:
                self.brand_title = "Nike, Inc. - Just Do It"
                self.brand_url = "https://www.nike.com"
                self.brand_summary = "Nike, Inc. is an American multinational corporation that is engaged in the design, development, manufacturing, and worldwide marketing and sales of footwear, apparel, equipment, accessories, and services."
            elif "apple" in name:
                self.brand_title = "Apple Inc. - Think Different"
                self.brand_url = "https://www.apple.com"
                self.brand_summary = "Apple Inc. is an American multinational technology company that specializes in consumer electronics, software, and online services."
            else:
                self.brand_title = f"{self.brand_name} - Official Website"
                self.brand_url = f"https://www.{name.replace(' ', '').lower()}.com"
                self.brand_summary = f"{self.brand_name} is a leading provider of innovative solutions in their sector, committed to delivering excellence and driving customer success through cutting-edge products."
            self.is_loading = False

    @rx.event
    async def complete_setup(self):
        self.is_setup_complete = True
        nav_state = await self.get_state(NavState)
        nav_state.set_step(1)
        yield rx.toast("Brand setup complete!", duration=3000, close_button=True)