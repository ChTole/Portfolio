import { Component, input } from '@angular/core';
import { PROFILE } from '../../data/profile';

@Component({
  imports: [],
  selector: 'app-social-links',
  styleUrl: './social-links.css',
  templateUrl: './social-links.html',
})
export class SocialLinks {
  size = input<'sm' | 'lg'>('sm');
  protected readonly profile = PROFILE;
}
