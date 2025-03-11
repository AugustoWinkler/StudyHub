package pokemon.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Component;

import jakarta.transaction.Transactional;
import pokemon.model.Pokemon;

@Component
public interface PokemonRepository extends JpaRepository<Pokemon, Integer> {

	@Modifying
	@Transactional
	@Query("UPDATE Pokemon p SET p.level = p.level + 1 WHERE p.id = :id")
	void levelUp(Integer id);
}
