import java.io.File

val fileName: String = "day_1_input.txt"
val targetSum: Int = 2020

fun day1(): Int {
    val mutableMap: MutableMap<Int, Any?> = emptyMap<Int, Any?>().toMutableMap()
    if (!File(fileName).isFile) return 0
    File(fileName).forEachLine { mutableMap[it.toInt()] = null }
    for (key in mutableMap.keys)
    {
        if (mutableMap.containsKey(targetSum - key))
        {
            return key * (targetSum - key)
        }
    }
    return 0
}

println(day1())
