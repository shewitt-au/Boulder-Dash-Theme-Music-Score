\version "2.16.0"

\header {
  title = "Boulder Dash (C64)"
  composer = "Peter Liepa"
  arranger = "Transcribed by Stephen Hewitt"
  tagline = "" % removed
}

\language english

\score
{
	\new PianoStaff \with { instrumentName = "SID chip" }
	<<
		\new Staff = "up"
		{
			<<
				\new Voice = "voice1"
				{
					\voiceOne
					{{key}}
					{{tempo}}
					\set midiInstrument = #"acoustic guitar (steel)"
					\autochange
					\repeat volta 2
					{
						{{voice1}}
					}
				}

				\new Voice = "voice2"
				{
					\voiceTwo
					{{key}}
					\set midiInstrument = #"electric guitar (jazz)"
					\autochange
					\repeat volta 2
					{

						{{voice2}}
					}
				}
			>>
		}

		\new Staff = "down"
		{
			\clef bass
			{{key}}
		}
	>>

	\layout { }
	\midi
	{
		\context
		{
			\Staff
			\remove "Staff_performer"
		}
		\context
		{
			\Voice
			\consists "Staff_performer"
		}
	}
}
