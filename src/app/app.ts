import { Component, inject, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Navbar } from './shared/navbar/navbar';
import { Footer } from './shared/footer/footer';
import { ViewportScroller } from '@angular/common';

@Component({
  imports: [
    Navbar, Footer, RouterOutlet
  ],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  
  constructor() {
    // Altura real del navbar + un margen, calculada en cada desplazamiento
    inject(ViewportScroller).setOffset(() => {
      const navbar = document.querySelector('nav');
      return [0, (navbar?.offsetHeight ?? 0) + 16];
    });
  }

  protected readonly title = signal('portfolio');
}
