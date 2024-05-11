import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Generate a math movie based on the given problem, audience age, and language.")
    parser.add_argument("math_problem", type=str,
                        help="The math problem to be visualized in the movie.")
    parser.add_argument("audience_type", type=int,
                        help="The target audience age for the math movie.")
    parser.add_argument("--language", type=str, default="English",
                        help="The language for the movie narration (default is English).")
    parser.add_argument("--voice_label", type=str, default="en-US-AriaNeural",
                        help="The voice label for the narration (default is en-US-AriaNeural).")

    args = parser.parse_args()

    # Placeholder for the function that creates the math movie
    create_math_matrix_movie(
        args.math_problem, args.audience_type, args.language, args.voice_label)


MOVIE_PROMPT = """

Can you explain {math_problem} to a {audience_type}? Please create python code for a manim video for the same. 

Please do not use any external dependencies like mp3s or svgs or graphics. If you need to draw something, do so using exclusively manim. 

Do use voiceovers to narrate the video. The following is an example of how to do that:

```
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class AzureExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            )
        )

        circle = Circle()
        square = Square().shift(2 * RIGHT)

        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)

        with self.voiceover(text="Let's shift it to the left 2 units.") as tracker:
            self.play(circle.animate.shift(2 * LEFT),
                      run_time=tracker.duration)

        with self.voiceover(text="Now, let's transform it into a square.") as tracker:
            self.play(Transform(circle, square), run_time=tracker.duration)

        with self.voiceover(
            text="You can also change the pitch of my voice like this.",
            prosody={{"pitch": "+40Hz"}},
        ) as tracker:
            pass

        with self.voiceover(text="Thank you for watching."):
            self.play(Uncreate(circle))

        self.wait()
```

The voice for the "{language}" is "{voice_label}". Please use this voice for the narration.

Please do not use any external dependencies like svgs since they are not available. Please use only manim for the video. Please write ALL the code needed since it will be extracted directly and run from your response. 


"""


def create_math_matrix_movie(math_problem, audience_type, language="English", voice_label="en-US-AriaNeural"):
    # Check if audience_type is a digit and format it as "x years old", otherwise leave as is
    if str(audience_type).isdigit():
        audience_type = f"{audience_type} year old"

    # Fill up the MOVIE_PROMPT with the provided arguments
    filled_prompt = MOVIE_PROMPT.format(
        math_problem=math_problem, audience_type=audience_type, language=language, voice_label=voice_label)

    # Print the filled prompt to the console
    print(filled_prompt)


if __name__ == "__main__":
    main()