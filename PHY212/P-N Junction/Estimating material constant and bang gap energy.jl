using Plots 
using DataFrames
using XLSX
using LsqFit
using LaTeXStrings




gr()




e = 1.60217662e-19
k = 1.38064852e-23
T = 298.15




reverse = DataFrame(XLSX.readtable("Reverse saturation current and material constant.xlsx", "Sheet1"))
reverse = DataFrame(Voltage = reverse[1, 1], Current = reverse[2, 1])
reverse[!, "ln(I)"] = log.(exp(1), (reverse.Current .* 1e-3))



linear_model(x, params) = params[1] .* x .+ params[2]

fit = curve_fit(linear_model, (reverse.Voltage)[3:end], 
    (reverse."ln(I)")[3:end], [0.5, 0.5])

params = fit.param
m, c = params
Δm, Δc = standard_errors(fit)



scatter(reverse[!, "Voltage"], reverse[!, "ln(I)"], markersize = 2,
    label = "Data")
x = LinRange(0.45, 0.75, 1000)
plot!(x, linear_model(x, params), label = "Best Fit", 
    color = "lawngreen", legend = :topleft, show = true)
title!(L"log_e(I)\quad  v/s\quad Voltage")
ylabel!(L"log_e(I)")
xlabel!(L"Voltage (V)")



I0 = exp(c) ##in A
I0 = I0 * 10^(9)

η = e/(m*k*T)

Δη = sqrt((Δm/m)^2)

println("Material Constant η = $η")
println("Standard Deviation = $Δη")
println("Reverse Saturation Current = $I0 nA")





TvsV = DataFrame(XLSX.readtable("Energy band gap and Temperature coefficient.xlsx", "Sheet1"))
TvsV = DataFrame(Temperature = TvsV[1, 1], Voltage = TvsV[2, 1])




linear_model(x, params) = params[1] .* x .+ params[2]

fit = curve_fit(linear_model, TvsV.Voltage, TvsV.Temperature, [0.5, 0.5])

params = fit.param
m, c = params
Δm, Δc = standard_errors(fit)




scatter(TvsV[!, "Voltage"], TvsV[!, "Temperature"], label = "Data", color = "blue", markersize = 2)
x = LinRange(0.59, 0.673, 1000)
plot!(x, linear_model(x, params), label = "Best Fit", color = "lawngreen", show = true)
title!("Voltage v/s Temperature")
ylabel!(L"Temperature (K)")
xlabel!(L"Voltage (V)")



Eg = 6.242e+18 * -(c/m)*e 
ΔEg = sqrt((Δm/m)^2 + (Δc/c)^2)

println("Band gap value = $Eg eV")
println("Standard Deviation = $ΔEg eV")



forward = DataFrame(XLSX.readtable("Forward characteristics of junction diode.xlsx", "Sheet1"))
forward = DataFrame(Voltage = forward[1, 1], Current = forward[2, 1])



exp_model(x, params) = params[1] .* exp.(params[2] .* x) .+ params[3]

fit = curve_fit(exp_model, forward.Voltage, forward.Current, [0.5, 0.5, 0.5])

params = fit.param
I0, r, c = params
ΔI0, Δr, Δc = standard_errors(fit)

scatter(forward[!, "Voltage"], forward[!, "Current"] , legend = :topleft, label = "Given Data")
x = LinRange(0.0, 0.65, 1000)
plot!(x, exp_model(x, params), label = "Best Fit", color = "lawngreen", legend = :topleft)
plot!( [0.55, 0.4], [6, 16], arrow = :closed, label = "", color = :black)
title!("Current v/s Voltage \n Forward Bias")
ylabel!(L"Current (I)")
xlabel!(L"Voltage (V)")
annotate!((0.4, 17, L"8.44 \times e^{19.37 V} - 0.19"), show = true)


