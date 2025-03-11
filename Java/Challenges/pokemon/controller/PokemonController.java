package pokemon.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import pokemon.model.Pokemon;
import pokemon.repository.PokemonRepository;

@RestController
@RequestMapping("/pokemon")
public class PokemonController {
	@Autowired
	PokemonRepository repository;

	@GetMapping("/showPokemons")
	public List<Pokemon> showPokemons() {
		return repository.findAll();
	}

	@PostMapping("/addPokemon")
	public void addPokemon(String name) {
		Pokemon pokemon = new Pokemon(name);
		repository.save(pokemon);
	}

	@DeleteMapping("/deletePokemon")
	public void deletePokemon(Integer id) {
		repository.deleteById(id);
	}

	@PutMapping("/levelUpPokemon")
	public void levelUpPokemon(Integer id) {
		repository.levelUp(id);
	}
}
