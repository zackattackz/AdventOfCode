using AOCRunner;

var solutions = SolutionsParse.TryGetSolutions(args[0]);

if (args.Length != 4 ||
    solutions is null ||
    !int.TryParse(args[1], out var year) ||
    !int.TryParse(args[2], out var day) ||
    !int.TryParse(args[3], out var part))
{
    Console.WriteLine("Usage: runner csharp <MONTH> <DAY>");
    return;
}

using var inputReader = InputReader.Get(year, day);

Console.WriteLine(solutions.Solve(year, day, part, inputReader));