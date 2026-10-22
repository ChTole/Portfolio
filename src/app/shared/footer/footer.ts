import { Component } from '@angular/core';
import { PROFILE } from '../../data/profile';
import { SocialLinks } from '../social-links/social-links';

@Component({
  imports: [SocialLinks],
  selector: 'app-footer',
  styleUrl: './footer.css',
  templateUrl: './footer.html',
})
export class Footer {
  protected readonly profile = PROFILE;
  protected readonly year = new Date().getFullYear();
}
