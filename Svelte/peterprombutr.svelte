<script>
	let cup = { cupEmpty: false };

	function toggle() {
		cup.cupEmpty = !cup.cupEmpty;
	}
</script>

{#if cup.cupEmpty}
	<h1>
		Here's your code ( • ∀•)–Ψ
	</h1>
	<button on:click={toggle}>
		Add more coffee?
	</button>
	
{/if}

{#if !cup.cupEmpty}
	<button on:click={toggle}>
		Drink your coffee ☕︎
	</button>
{/if}