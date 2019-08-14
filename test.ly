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
				\autochange
				{
					g, b, d g a, c d a ds f g as f e' fs d' g, g d, a, f, a a, f, g, g d, a, ds g' g ds f, f c, g, cs f' f cs d, fs e, g c c c' c g g g g g g g g g g g g g g g g g g g g g g g g g g g g f f f f g g' g f' g e' g d' f f' f f' f c' f f' g g g g g g g g g g g g f f f f b g d b, a f c f, b g d b, a f c f,
				}
			}

			\new Voice = "voice2"
			{
				\voiceTwo
				\autochange
				{
					g,, d, g, as, f,, e, f, c e'' e'' ds, e'' f, c' fs, as g,, g,, g,, g,, f,, f,, f,, f,, g,, g,, g,, g,, ds, ds, ds, ds, f,, f,, f,, f,, cs, cs, cs, cs, ds'' d ds'' d cs'' cs'' g,, g,, g,, g,, g,, g,, g, g, g,, g,, f,, f,, f,, f,, f, f, f,, f,, g,, b g,, c' g, b g,, c' f,, b f,, c' f, a f,, as g,, g,, g,, d' g, g, g,, as f,, f,, f,, f,, f, f, f,, f,, g,, b g,, c' g, b g,, c' f,, b f,, c' f, a f,, as g d b, g, f c a, f,, d' b g d c a, f, f,,
				}
			}
		>>
		}

	\new Staff = "down" { \clef bass }
	>>

	\layout { }
	\midi { }
}
