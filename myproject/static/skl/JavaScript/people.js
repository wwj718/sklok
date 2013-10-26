// JavaScript Document
$(document).ready(function(){
	
	//导航
	$("li#people").bind("mouseover",function(){
		$("ul.people").show();
		$("li#people>a").css({"color":"#0083a9","font-weight":"bold"});
		
	})
	$("li#people").bind("mouseout",function(){
		$("ul.people").hide();
	})
	$("li#research").bind("mouseover",function(){
		$("ul.research").show();
		$("li#research>a").css({"color":"#0083a9","font-weight":"bold"});
		
	})
	
	
	$("li#research").bind("mouseout",function(){
		$("ul.research").hide();
		$("li#research>a").css({"color":"#000","font-weight":"normal"})
	})
	$("li#newsevents").bind("mouseover",function(){
		$("ul.newsevents").show();
		$("li#newsevents>a").css({"color":"#0083a9"});
		
	})
	$("li#newsevents").bind("mouseout",function(){
		$("ul.newsevents").hide();
		$("li#newsevents>a").css({"color":"#000","font-weight":"normal"});
	})
	$("li#facilities").bind("mouseover",function(){
		$("ul.facilities").show();
		$("li#facilities>a").css({"color":"#0083a9","font-weight":"bold"});
		
	})
	$("li#facilities").bind("mouseout",function(){
		$("ul.facilities").hide();
		$("li#facilities>a").css({"color":"#000","font-weight":"normal"})
	})
	/*
	*/
	
	
	
	
	
	
	
	
	
	//图片切换
	var timedMsg=setInterval(function()
	{
		var a=setTimeout(function(){
			$("img.picture1").fadeOut(1000);
		},3000)
		var b=setTimeout(function(){
			$("img.picture2").fadeOut(1000);
		},6000)
		var c=setTimeout(function(){
			$("img.picture3").fadeOut(1000);
		},9000)
		var d=setTimeout(function(){
			$("img.picture4").fadeOut(1000);
		},12000);
		var e=setTimeout(function(){
			$("img.picture1").fadeIn(1);
		},12000);
		var f=setTimeout(function(){
			$("img.picture2").fadeIn(1);
		},12000);
		var g=setTimeout(function(){
			$("img.picture3").fadeIn(1);
		},12000);
		var h=setTimeout(function(){
			$("img.picture4").fadeIn(1);
		},12000);
		
	},12000)	
		

});