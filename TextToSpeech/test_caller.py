import text_to_speech as ts


e = ts.ElevenLabs()

e.set_recordings(['Recordings/rec1.mp3', 'Recordings/rec2.mp3', 'Recordings/rec3.mp3'])
e.clone('test', 'test')
e.set_text('Nam strzelać nie kazano. — Wstąpiłem na działo'
    'I spojrzałem na pole; dwieście armat grzmiało.'
    'Artyleryji ruskiéj ciągną się szeregi,'
    'Prosto, długo, daleko, jako morza brzegi;'
    'I widziałem ich wodza; — przybiegł, mieczem skinął'
    'I jak ptak jedno skrzydło wojska swego zwinął.'
    'Wylewa się spod skrzydła ściśniona piechota'
    'Długą, czarną kolumną, jako lawa błota,'
    'Nasypana iskrami bagnetów. Jak sępy,'
    'Czarne chorągwie na śmierć prowadzą zastępy.')
e.play()
