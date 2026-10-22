import { Component, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { PROFILE } from '../../data/profile';

@Component({
  imports: [RouterLink],
  selector: 'app-navbar',
  styleUrl: './navbar.css',
  templateUrl: './navbar.html',
})
export class Navbar {
  protected readonly profile = PROFILE;
  protected readonly menuOpen = signal(false);
 
  protected readonly links = [
    { label: 'Proyectos', fragment: 'proyectos' },
    { label: 'Habilidades', fragment: 'habilidades' },
    { label: 'Sobre mí', fragment: 'sobre-mi' },
    { label: 'Contacto', fragment: 'contacto' },
  ];
 
  protected toggleMenu(): void {
    this.menuOpen.update(open => !open);
  }
}
