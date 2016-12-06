(defproject adventofclojure "2016.0.0"
  :description "Solutions to the Advent of Code puzzles."
  :url "https://github.com/tau-/advent-of-code-2016"
  :license {:name "MIT"
            :url "https://opensource.org/licenses/MIT"}
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [org.clojure/data.json "0.2.6"]
                 [org.clojure/math.combinatorics "0.1.3"]
                 [digest "1.4.4"]]
  :main ^:skip-aot adventofclojure.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
