﻿module AOCfsharp

type Solutions() =
    interface AOCSolutions.ISolutions with
        member this.Solve (year: int, day: int, part: int, input: System.IO.TextReader): string = 
                    raise (System.NotImplementedException())

[<Literal>]
let SolutionsName = "fsharp"