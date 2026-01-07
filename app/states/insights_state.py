import reflex as rx
import random


class InsightsState(rx.State):
    competitive_data: list[dict[str, str | int]] = [
        {"name": "Your Brand", "mentions": 4500, "rank": 1, "fill": "#fb4e0b"},
        {"name": "Competitor A", "mentions": 3200, "rank": 2, "fill": "#005071"},
        {"name": "Competitor B", "mentions": 2800, "rank": 3, "fill": "#ababab"},
        {"name": "Competitor C", "mentions": 1500, "rank": 4, "fill": "#e6e6e6"},
    ]
    consumer_attributes: list[dict[str, str | int]] = [
        {"attribute": "Price Sensitivity", "weight": 85, "fill": "#fb4e0b"},
        {"attribute": "Brand Loyalty", "weight": 65, "fill": "#005071"},
        {"attribute": "Tech Savviness", "weight": 45, "fill": "#ababab"},
        {"attribute": "Sustainability Focus", "weight": 70, "fill": "#ff906d"},
    ]
    persona_visibility_data: list[dict[str, str | int]] = [
        {"month": "Jan", "Value Seeker": 30, "Trend Hunter": 20, "Performance Pro": 50},
        {"month": "Feb", "Value Seeker": 45, "Trend Hunter": 25, "Performance Pro": 40},
        {"month": "Mar", "Value Seeker": 35, "Trend Hunter": 40, "Performance Pro": 60},
        {"month": "Apr", "Value Seeker": 50, "Trend Hunter": 35, "Performance Pro": 55},
        {"month": "May", "Value Seeker": 60, "Trend Hunter": 50, "Performance Pro": 45},
        {"month": "Jun", "Value Seeker": 75, "Trend Hunter": 60, "Performance Pro": 70},
    ]
    topic_data: list[dict[str, str | int]] = [
        {"topic": "Sustainability", "count": 85},
        {"topic": "Price Point", "count": 72},
        {"topic": "Comfort", "count": 65},
        {"topic": "Durability", "count": 45},
        {"topic": "Innovation", "count": 30},
    ]
    source_data: list[dict[str, str | int]] = [
        {"name": "twitter.com", "value": 45, "fill": "#fb4e0b"},
        {"name": "reddit.com", "value": 25, "fill": "#005071"},
        {"name": "techcrunch.com", "value": 20, "fill": "#ff906d"},
        {"name": "cnet.com", "value": 10, "fill": "#ababab"},
    ]
    sentiment_score: int = 78
    sentiment_distribution: list[dict[str, str | int]] = [
        {"type": "Positive", "value": 65, "color": "bg-green-500"},
        {"type": "Neutral", "value": 25, "color": "bg-gray-400"},
        {"type": "Negative", "value": 10, "color": "bg-red-500"},
    ]
    word_cloud: list[dict[str, str]] = [
        {"text": "Quality", "size": "text-3xl", "color": "text-[#fb4e0b]"},
        {"text": "Innovative", "size": "text-2xl", "color": "text-[#005071]"},
        {"text": "Expensive", "size": "text-xl", "color": "text-gray-500"},
        {"text": "Durable", "size": "text-xl", "color": "text-[#fb4e0b]"},
        {"text": "Comfortable", "size": "text-lg", "color": "text-green-600"},
        {"text": "Stylish", "size": "text-lg", "color": "text-purple-600"},
        {"text": "Reliable", "size": "text-base", "color": "text-blue-500"},
        {"text": "Support", "size": "text-base", "color": "text-orange-400"},
        {"text": "Fast", "size": "text-sm", "color": "text-gray-400"},
        {"text": "Eco-friendly", "size": "text-sm", "color": "text-teal-500"},
    ]
    heatmap_data: list[dict[str, str | int]] = [
        {"label": "Value Seeker", "c1": 80, "c2": 40, "c3": 20},
        {"label": "Trend Hunter", "c1": 30, "c2": 90, "c3": 50},
        {"label": "Performance Pro", "c1": 60, "c2": 20, "c3": 85},
    ]
    topic_matrix_data: list[dict[str, str | int]] = [
        {"label": "Sustainability", "c1": 70, "c2": 85, "c3": 40},
        {"label": "Price Point", "c1": 50, "c2": 40, "c3": 90},
        {"label": "Innovation", "c1": 85, "c2": 60, "c3": 55},
    ]
    competitor_names: list[str] = ["Comp A", "Comp B", "Comp C"]

    @rx.event
    def get_opacity(self, value: int) -> str:
        if value > 80:
            return "bg-[#fb4e0b]/90"
        if value > 60:
            return "bg-[#fb4e0b]/70"
        if value > 40:
            return "bg-[#fb4e0b]/40"
        return "bg-[#fb4e0b]/10"