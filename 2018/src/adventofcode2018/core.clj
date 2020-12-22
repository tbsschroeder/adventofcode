(ns adventofcode2018.core
  (:require [adventofcode2018.day01 :as day01]
            [adventofcode2018.day02 :as day02]
            [adventofcode2018.day03 :as day03]
            [adventofcode2018.day04 :as day04]
            [adventofcode2018.day05 :as day05]
            [adventofcode2018.day06 :as day06]
            [adventofcode2018.day07 :as day07]))

  (defn main []
    (println "Day 01 Part 1" (day01/my_frequency day01/input))
    (println "Day 01 Part 2" (day01/my_occurrence day01/input))
    (println "Day 02 Part 1" (day02/checksum day02/input))
    (println "Day 02 Part 2" (day02/hamming day02/input))
    (println "Day 03 Part 1" (day03/intact-claims day03/input))
    (println "Day 03 Part 2" (day03/overlapping-claims day03/input))
    (println "Day 04 Part 1" (day04/maxsleep day04/input))
    (println "Day 04 Part 2" (day04/part2 day04/input))
    (println "Day 05 Part 1" (day05/polymer day05/input))
    (println "Day 05 Part 2" (day05/shortest-polymer day05/input))
    (println "Day 06 Part 1" (day06/part1 day06/input))
    (println "Day 06 Part 2" (day06/part2 day06/input))
    (println "Day 07 Part 1" (day07/instructions day07/input))
    (println "Day 07 Part 2" (day07/part2 day07/input)))
