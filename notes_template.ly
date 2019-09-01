\version "2.16.0"

\header {
  tagline = "" % removed
}

\paper
{
	indent = 0\cm
	paper-height = 90\mm
}

\language english

upper =
{
  \clef treble
  {{right_hand}}
}

lower =
{
  \clef bass
  {{left_hand}}
}

\score
{
	\new PianoStaff
	<<
		\new Staff = "upper" \upper
		\new Staff = "lower" \lower
	>>
}
