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

\score
{
	\new PianoStaff
	\autochange
	{
		{{notes}}
	}
}
