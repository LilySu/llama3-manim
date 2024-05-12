from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class FivePlusThree(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )
        
        # Create apples
        apples = VGroup(*[Circle(radius=0.3, color=RED) for _ in range(8)])
        apples.arrange(RIGHT, buff=0.5)
        
        # Five apples
        five_apples = apples[:5]
        five_text = Text("5", font_size=60).next_to(five_apples, UP)
        
        # Three apples
        three_apples = apples[5:]
        three_text = Text("3", font_size=60).next_to(three_apples, UP)
        
        # Plus and equal signs
        plus_sign = Text("+", font_size=60).move_to(apples.get_center() + UP)
        equal_sign = Text("=", font_size=60).next_to(apples, RIGHT)
        
        # Eight text
        eight_text = Text("8", font_size=60).next_to(equal_sign, RIGHT)
        
        # Animation
        with self.voiceover(text="Let's learn how to add 5 plus 3.") as tracker:
            self.play(Create(five_apples), run_time=tracker.duration)

        with self.voiceover(text="Here are 5 red apples.") as tracker:
            self.play(FadeIn(five_text), run_time=tracker.duration)

        with self.voiceover(text="Now, we'll add 3 more apples.") as tracker:
            self.play(Create(three_apples), run_time=tracker.duration)

        with self.voiceover(text="Here are the 3 more apples.") as tracker:
            self.play(FadeIn(three_text), run_time=tracker.duration)

        with self.voiceover(text="When we add them together, we use the plus sign.") as tracker:
            self.play(FadeIn(plus_sign), run_time=tracker.duration)

        with self.voiceover(text="To show the answer, we use the equal sign.") as tracker:
            self.play(FadeIn(equal_sign), run_time=tracker.duration)

        with self.voiceover(text="Let's count all the apples together: 1, 2, 3, 4, 5, 6, 7, 8!") as tracker:
            self.play(FadeIn(eight_text), run_time=tracker.duration)

        with self.voiceover(text="So, 5 plus 3 equals 8.") as tracker:
            self.play(FadeOut(five_text, three_text, plus_sign), run_time=tracker.duration)
            self.play(apples.animate.arrange(RIGHT, buff=0.2), run_time=tracker.duration)

        self.wait()