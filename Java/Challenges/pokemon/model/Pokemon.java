package pokemon.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.ToString;

@Entity
@NoArgsConstructor
@RequiredArgsConstructor
@ToString
public class Pokemon {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "id")
	private Integer id;
	@Column(length = 20, name = "name")
	@Getter
	@NonNull
	private String name;
	@Column(name = "level")
	@Getter
	private int level = 0;
}
