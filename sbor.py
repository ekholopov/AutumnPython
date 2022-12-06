import sonar
import signals

water = signals.Water()
(time, signalleft, signalright) = water.get_signals(500, 30)

sonar.Sonar().get_coordinates(signalleft, signalright)
