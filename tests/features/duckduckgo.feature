Feature: DuckDuckGo Instant Answer API
  As a user,
  I want to find US Presidents on DuckDuckGo

Scenario Outline: Search DuckDuckGo API for US Presidents
  Given the DuckDuckGo API is queried for US Presidents
  Then the response contains results for "<president>"
  Examples: Presidents
    | president |
    |Washington |
    |Adams      |
    |Jefferson  |
    |Madison    |
    |Monroe     |
    |Jackson    |
    |Van Buren  |
    |Harrison   |
    |Tyler      |
    |Polk       |
    |Taylor     |
    |Fillmore   |
    |Pierce     |
    |Buchanan   |
    |Lincoln    |
    |Johnson    |
    |Grant      |
    |Hayes      |
    |Garfield   |
    |Arthur     |
    |Cleveland  |
    |McKinley   |
    |Roosevelt  |
    |Taft       |
    |Wilson     |
    |Harding    |
    |Coolidge   |
    |Hoover     |
    |Truman     |
    |Eisenhower |
    |Kennedy    |
    |Nixon      |
    |Ford       |
    |Carter     |
    |Reagan     |
    |Bush       |
    |Clinton    |
    |Obama      |
    |Trump      |
