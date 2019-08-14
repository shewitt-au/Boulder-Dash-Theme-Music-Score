\version "2.16.0"

\header { 
  tagline = ""  % removed 
}

\language english

\score
{
	\new PianoStaff
	<<
		\new Staff = "up"
		{
			<<
				\new Voice = "voice1"
				{
					\voiceOne
					\tempo 4 = 180
					\set midiInstrument = #"acoustic guitar (steel)"
					\autochange
					{
						f8 a c' f' g as c' g' cs' ds' f' gs' ds' d'' e' c'' f f' c g ds g' g ds f f' c g cs' f'' f' cs' ds ds' as, f b ds'' ds' b c e' d f' as as as' as f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' f' ds' ds' ds' ds' f' f'' f' ds'' f' d'' f' c'' ds' ds'' ds' ds'' ds' as' ds' ds'' f' f' f' f' f' f' f' f' f' f' f' f' ds' ds' ds' ds' a' f' c' a g' ds' as ds a' f' c' a g' ds' as ds 
					}
				}

				\new Voice = "voice2"
				{
					\voiceTwo
					\set midiInstrument = #"electric guitar (jazz)"
					\autochange
					{

						f,8 c f gs ds, d ds as cs, cs, cs cs, ds as' e gs' f, f, f, f, ds, ds, ds, ds, f, f, f, f, cs cs cs cs ds, ds, ds, ds, b, b, b, b, c, c' c, c' as,, as,, f, f, f, f, f, f, f f f, f, ds, ds, ds, ds, ds ds ds, ds, f, a' f, as' f a' f, as' ds, a' ds, as' ds g' ds, gs' f, f, f, c'' f f f, gs' ds, ds, ds, ds, ds ds ds, ds, f, a' f, as' f a' f, as' ds, a' ds, as' ds g' ds, gs' f' c' a f ds' as g ds, c'' a' f' c' as g ds ds, 
					}
				}
			>>
		}

		\new Staff = "down"
		{
			\clef bass
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
