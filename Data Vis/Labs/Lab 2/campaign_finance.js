var cands = [{"Candidate":"Jeb Bush","Party":"Republican","q2":"11429897.64","q4":"31922099.87", "final":"35491191.48"},
             {"Candidate":"Ben Carson","Party":"Republican","q2":"10642242.10","q4":"54036610.31", "final":"65091035.97"},
             {"Candidate":"Ted Cruz","Party":"Republican","q2":"14349160.55","q4":"47086857.05", "final":"94338654.84"},
             {"Candidate":"John Kasich","Party":"Republican","q2":null,"q4":"7582364.84", "final":"19692691.23"},
             {"Candidate":"Marco Rubio","Party":"Republican","q2":"8876868.37","q4":"28792145.51", "final":"48331861.99"},
             {"Candidate":"Donald Trump","Party":"Republican","q2":null,"q4":"19405216.96", "final":"350668435.70"},
             {"Candidate":"Hillary Clinton","Party":"Democratic","q2":"47549949.64","q4":"115563928.67", "final":"585666688.73"},
             {"Candidate":"Bernie Sanders","Party":"Democratic","q2":"15247353.43","q4":"75023151.54", "final":"237640609.52"}];

pacs = [{"PAC":"Right to Rise","Candidate":"Jeb Bush","q2":"103167845.8","q4":"118307035.5", "final":"121695224 "},
        {"PAC":"2016 Cmte","Candidate":"Ben Carson","q2":"3827445.21","q4":"9968830.43", "final":"15020143 "},
        {"PAC":"National Draft Ben Carson for President Cmte","Candidate":"Ben Carson","q2":"3368222.78","q4":"3563717.01", "final":"3567902"},
        {"PAC":"Keep the Promise I","Candidate":"Ted Cruz","q2":"11007096","q4":"11036750.4", "final":"11036750.4"},
        {"PAC":"Keep the Promise II","Candidate":"Ted Cruz","q2":"10000000","q4":"10000000", "final":"10000000"},
        {"PAC":"Keep the Promise III","Candidate":"Ted Cruz","q2":"15000000","q4":"15398394.01", "final":"17245945"},
        {"PAC":"Keep the Promise PAC","Candidate":"Ted Cruz","q2":"1826500","q4":"2569257", "final":"5188867"},
        {"PAC":"Stand for Truth","Candidate":"Ted Cruz","q2":null,"q4":"2474201.64", "final":"11,289,939"},
        {"PAC":"Conservative Solutions PAC","Candidate":"Marco Rubio","q2":"16057755","q4":"30449901", "final":"60564219"},
        {"PAC":"Reclaim America PAC","Candidate":"Marco Rubio","q2":"1258026.55","q4":"1271821.17", "final":"1467401"},
        {"PAC":"New Day for America","Candidate":"John Kasich","q2":null,"q4":"3455863.76", "final":"15596477"},
        {"PAC":"Make America Great Again","Candidate":"Donald Trump","q2":null,"q4":"1732684", "final":"1742684"},
        {"PAC":"Priorities USA Action","Candidate":"Hillary Clinton","q2":"15674062.44","q4":"41002513.08", "final":"192065768"},
        {"PAC":"Ready PAC","Candidate":"Hillary Clinton","q2":"3180592.94","q4":"3465425.32", "final":"3621815.7"},
        {"PAC":"Correct the Record","Candidate":"Hillary Clinton","q2":"1435097.81","q4":"3436572.4", "final":"9710340.2"}];

function createInitialScatterplot() {   
    var margin = {top: 20, right: 20, bottom: 40, left: 40};
    var width = 400 - margin.left - margin.right;
    var height = 400 - margin.top - margin.bottom;

    // create an SVG using the D3 Margins Convention
    // http://bl.ocks.org/mbostock/3019563
    var svg = d3.select("#scatter").append("svg")
	.attr("width", width + margin.left + margin.right)
	.attr("height", height + margin.top + margin.bottom)
	.append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    svg.selectAll("circle.republican")
	.data(d3.range(0,4))
	.enter().append("circle")
	.attr("cx", function(d,i) { return 4 * i * i + 60*i + 30; })
	.attr("cy", function(d,i) { return (15-i) * 15 + 15; })
	.attr("r", 5) 
	.attr("class", "republican")
	.attr("fill", "red")

    svg.selectAll("circle.democratic")
	.data(d3.range(0,4))
	.enter().append("circle")
	.attr("cx", function(d,i) { return (16-3*i) * (16-3*i) + 20*i; })
	.attr("cy", function(d,i) { return i * 30 + 2 * (70-i); })
	.attr("r", 5) 
	.attr("class", "democratic")
	.attr("fill", "blue")
    
}
