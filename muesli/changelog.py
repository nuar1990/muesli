# -*- coding: utf-8 -*-
#
# utils.py
#
# This file is part of MUESLI.
#
# Copyright (C) 2012, Matthias Kuemmerer <matthias (at) matthias-k.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

changelog=u"""
====2017-11-30
concerns:users,assistants,tutors
Alle Bugs im MÜSLI sind jetzt in den IssueTracker von Github umgezogen. Dort
können gerne weitere programmtechnische Probleme gemeldet werden. Support
für die Installation im Mathematischen Institut gibt es weiterhin über die
unter Kontakt genannte Adresse.

====2016-02-19
concerns:users,assistants,tutors
In den nächsten Wochen zieht die Fakultät für Mathematik und Informatik
gemeinsam mit dem IWR in das neu gebaute Mathematikon (INF 205). Aus diesem
Grund wird das MÜSLI um den 10. März teilweise nicht zur Verfügung stehen.

====2015-09-22
concerns:users
Ab sofort können sich Benutzer ohne Matrikelnummer anmelden, indem sie die
Matrikelnummer 00000 eingeben. Diese muss baldmöglichst nachgetragen werden um
Problemen beim eintragen der Prüfungsergebnisse aus dem Weg zu gehen.

====2014-08-30
concerns:assistants,tutors
Um Seminare sinnvoller Sortieren zu können werden Übungsgruppen ab sofort nach
Wochentag, Uhrzeit und Kommentarfeld (in dieser Reihenfolge) sortiert. Dadurch
wird ermöglicht, dass Seminare über das Kommentarfeld durchnummeriert werden
können.

====2012-10-19
concerns:assistants,tutors
Es gibt wieder Korrelationsdiagramme, zumindest für einzelne Testate und die Summe
der Übungszettel. Der Vergleich einzelner Aufgaben wird irgendwann noch implementiert.
Die Links zu den Korrelationsdiagrammen finden sich auf den Vorlesungs- und Übungsgruppenseiten
unter den Testaten.

====2012-09-22
concerns:assistants
Man kann jetzt Studenten per Hand in eine Vorlesung eintragen. Dazu gibt es auf
der Seite "Vorlesung bearbeiten" unten einen Link "Student als Teilnehmer eintragen".
Dort kann man durch Angabe der Emailadresse des Studenten diesen in eine Übungsgruppe
eintragen. Dieses Feature ist vor allem gedacht, um Studenten, die die Zulassung
zu einer Klausur in einem früheren Semester erworben haben, in die Vorlesesung
eintragen zu können. Sonst kann man ihnen keine Klausurpunkte eintragen.

====2012-09-14
concerns:assistants
Auf der Seite zum Noteneintragen gibt es nun den versprochenen Button, um einzelne
Zeilen abzuspeichern. Damit besteht nichtmehr die Gefahr, beim Eintragen der
Punkteänderung eines Studenten ausversehen alles zu überschreiben.

====2012-08-17
concerns:assistants
Von der Seite zum Noteneintragen aus kann man jetzt auch direkt die Punkte der
verlinkten Klausuren korrigieren. Dies ist gedacht, um nach der Klausureinsicht
Arbeitsschritte einzusparen. Die neue Note wird berechnet, aber nicht übertragen.
Dies muss man also noch selber machen. Demnächst wird es noch einen Button geben,
der dies übernehmen kann.

====2012-07-27
concerns:assistants
Um mit den neuen Regelungen für Multiple Choice-Aufgaben umgehen zu können, kennt die
Notenberechnung jetzt die Funktion "round3down", die auf Drittelnoten abrundet. Genaueres
findet sich in der Hilfe auf der Seite "Noten eintragen".

====2012-07-20
concerns:assistants,tutors
Die Seite mit der Punkteübersicht kann jetzt auch von Assistenten für die ganze Vorlesung
angezeigt werden. Der Link findet sich unten auf der Vorlesungsseite. Außerdem kann die
Tabelle durch Klick auf die Spaltenüberschriften nach den unterschiedlichen Werten sortiert
werden.

====2012-06-29
concerns:assistants
Neben Zulassung und Anmeldung können zu Klausuren jetzt auch Atteste verwaltet werden. Das
Konzept ist das gleiche wie bei Zulassung und Anmeldung: Man muss die Funktionalität bei
den Einstellungen des Testats freischalten. Danach findet sich beim Punkte-Eintragen der Link
zum Eintragen der Attest-Informationen. Außerdem wird auf der Seite zum Noteneintragen bei
verlinkten Testaten mit Attest der Atteststatus angezeigt.

====2012-06-19
concerns:assistants,tutors
Auf der Statistikseite zu Testaten kann jetzt eine Tabelle angezeigt werden, die angibt,
wieviele Studenten welche Mindestpunktzahl haben.

====2012-05-18
concerns:assistants
Ab jetzt können Übungsaufgaben und Testate gelöscht werden. Aufgaben können gelöscht werden,
wenn kein Punkte eingetragen sind (auch nicht bei bereits ausgetragenen Studenten!). Ein
Testat kann gelöscht werden, wenn es keine Aufgaben mehr hat.

====2012-04-18
concerns:assistants
Ab sofort können komplett leere Übungsgruppen gelöscht werden. In der Liste der ausgetretenen
Studenten werden Studenten die aus einer später gelöschten Gruppe ausgetreten sind, mit "gelöschte
Gruppe" angezeigt. Es lässt sich damit nicht mehr feststellen, aus welcher Gruppe sie genau
ausgetreten sind.

====2012-04-13
concerns:assistants
Vorlesungen können jetzt mehr als einen Assistenten haben. Weitere Assistenten können momentan
nur die Administratoren hinzufügen (Erreichbar über "Kontakt").

====2012-03-16
concerns:assistants
Das Ausrechnen von Noten hat eine Vereinfachung erfahren: Es gibt die zusätzlichen Funktionen
cases1, cases2 und cases3 zum Vergeben von ganzen, halben und drittel Noten. Details finden sich
unter "Hilfe" auf der Seite zum Noteneintragen.

====2012-03-02
concerns:assistants
Es ist jetzt möglich, für jede Vorlesung einzustellen, ob die Tutoren Punkte für alle
Übungsgruppen oder nur für ihre eigenen Übungsgruppen eintragen dürfen, oder auch, dass
sie gar keine Punkte eintragen dürfen. Die Option dazu findet sich auf der "Bearbeiten"-Seite
der Vorlesung.

====2012-02-27
concerns:assistants
Es gibt eine neue Seite mit Details zur Anmeldung über Präferenzen. Sie enthält Histogramme,
die die Beliebtheit jedes möglichen Termines angeben, sowie eine Übersicht der Fächerverteilung
unter den angemeldeten Studenten. Der Link zu der Seite findet sich auf der "Bearbeiten"-Seite
der Vorlesung.

====2012-02-02
concerns:assistants
Die Punkte von Testaten können versteckt werden. Dies bewirkt, dass die Studenten ihre
Punktzahlen in diesem Testat nicht sehen. Die Option findet sich auf der "Bearbeiten"-Seite
des Testats.
"""
