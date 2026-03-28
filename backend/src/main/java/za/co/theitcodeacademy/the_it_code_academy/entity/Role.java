package za.co.theitcodeacademy.theitcodeacademy.entity;

import jakarta.persistence.*;
import lombok.*;

@entity
@Table(name = "roles")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class Role {
    @Id 
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true, nullable = false)
    private String name; //e.g, "STUDENT"
}