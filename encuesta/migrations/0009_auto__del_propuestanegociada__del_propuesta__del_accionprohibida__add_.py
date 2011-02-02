# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'PropuestaNegociada'
        db.delete_table('encuesta_propuestanegociada')

        # Deleting model 'Propuesta'
        db.delete_table('encuesta_propuesta')

        # Deleting model 'AccionProhibida'
        db.delete_table('encuesta_accionprohibida')

        # Adding field 'ConocimientoLey.padre_golpea'
        db.add_column('encuesta_conocimientoley', 'padre_golpea', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True), keep_default=False)

        # Adding field 'ConocimientoLey.maestro_castiga'
        db.add_column('encuesta_conocimientoley', 'maestro_castiga', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True), keep_default=False)

        # Adding field 'ConocimientoLey.maestro_relacion'
        db.add_column('encuesta_conocimientoley', 'maestro_relacion', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True), keep_default=False)

        # Adding field 'ConocimientoLey.joven_case'
        db.add_column('encuesta_conocimientoley', 'joven_case', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True), keep_default=False)

        # Adding field 'ConocimientoLey.joven_relacion'
        db.add_column('encuesta_conocimientoley', 'joven_relacion', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True), keep_default=False)

        # Adding field 'ConocimientoLey.patron_acoso'
        db.add_column('encuesta_conocimientoley', 'patron_acoso', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True), keep_default=False)

        # Adding field 'ConocimientoLey.lider_religioso'
        db.add_column('encuesta_conocimientoley', 'lider_religioso', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True), keep_default=False)

        # Adding field 'ConocimientoLey.adulto_relacion'
        db.add_column('encuesta_conocimientoley', 'adulto_relacion', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True), keep_default=False)

        # Adding field 'ConocimientoLey.adulto_dinero'
        db.add_column('encuesta_conocimientoley', 'adulto_dinero', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True), keep_default=False)

        # Adding field 'CalidadAtencion.propuesta'
        db.add_column('encuesta_calidadatencion', 'propuesta', self.gf('django.db.models.fields.CharField')(default='', max_length=10), keep_default=False)

        # Adding field 'CalidadAtencion.si_tipo'
        db.add_column('encuesta_calidadatencion', 'si_tipo', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'CalidadAtencion.no_porque'
        db.add_column('encuesta_calidadatencion', 'no_porque', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'CalidadAtencion.propuesta2'
        db.add_column('encuesta_calidadatencion', 'propuesta2', self.gf('django.db.models.fields.CharField')(default='', max_length=10), keep_default=False)

        # Adding field 'CalidadAtencion.si_tipo2'
        db.add_column('encuesta_calidadatencion', 'si_tipo2', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'CalidadAtencion.no_porque2'
        db.add_column('encuesta_calidadatencion', 'no_porque2', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'PropuestaNegociada'
        db.create_table('encuesta_propuestanegociada', (
            ('si_tipo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('calidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.CalidadAtencion'])),
            ('propuesta', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('no_porque', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('encuesta', ['PropuestaNegociada'])

        # Adding model 'Propuesta'
        db.create_table('encuesta_propuesta', (
            ('si_tipo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('calidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.CalidadAtencion'])),
            ('propuesta', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('no_porque', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('encuesta', ['Propuesta'])

        # Adding model 'AccionProhibida'
        db.create_table('encuesta_accionprohibida', (
            ('adulto_dinero', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('patron_acoso', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('lider_religioso', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('adulto_relacion', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('maestro_castiga', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('joven_relacion', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('maestro_relacion', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('conocimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.ConocimientoLey'])),
            ('joven_case', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('padre_golpea', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
        ))
        db.send_create_signal('encuesta', ['AccionProhibida'])

        # Deleting field 'ConocimientoLey.padre_golpea'
        db.delete_column('encuesta_conocimientoley', 'padre_golpea')

        # Deleting field 'ConocimientoLey.maestro_castiga'
        db.delete_column('encuesta_conocimientoley', 'maestro_castiga')

        # Deleting field 'ConocimientoLey.maestro_relacion'
        db.delete_column('encuesta_conocimientoley', 'maestro_relacion')

        # Deleting field 'ConocimientoLey.joven_case'
        db.delete_column('encuesta_conocimientoley', 'joven_case')

        # Deleting field 'ConocimientoLey.joven_relacion'
        db.delete_column('encuesta_conocimientoley', 'joven_relacion')

        # Deleting field 'ConocimientoLey.patron_acoso'
        db.delete_column('encuesta_conocimientoley', 'patron_acoso')

        # Deleting field 'ConocimientoLey.lider_religioso'
        db.delete_column('encuesta_conocimientoley', 'lider_religioso')

        # Deleting field 'ConocimientoLey.adulto_relacion'
        db.delete_column('encuesta_conocimientoley', 'adulto_relacion')

        # Deleting field 'ConocimientoLey.adulto_dinero'
        db.delete_column('encuesta_conocimientoley', 'adulto_dinero')

        # Deleting field 'CalidadAtencion.propuesta'
        db.delete_column('encuesta_calidadatencion', 'propuesta')

        # Deleting field 'CalidadAtencion.si_tipo'
        db.delete_column('encuesta_calidadatencion', 'si_tipo')

        # Deleting field 'CalidadAtencion.no_porque'
        db.delete_column('encuesta_calidadatencion', 'no_porque')

        # Deleting field 'CalidadAtencion.propuesta2'
        db.delete_column('encuesta_calidadatencion', 'propuesta2')

        # Deleting field 'CalidadAtencion.si_tipo2'
        db.delete_column('encuesta_calidadatencion', 'si_tipo2')

        # Deleting field 'CalidadAtencion.no_porque2'
        db.delete_column('encuesta_calidadatencion', 'no_porque2')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.accesocontrolrecurso': {
            'Meta': {'object_name': 'AccesoControlRecurso'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'recursos'", 'symmetrical': 'False', 'to': "orm['encuesta.Recurso']"}),
            'recursos_decide': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'recursos_decide'", 'symmetrical': 'False', 'to': "orm['encuesta.Recurso']"})
        },
        'encuesta.accionvbg': {
            'Meta': {'object_name': 'AccionVBG'},
            'accion_tomar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.QueDebeHacer']", 'symmetrical': 'False'}),
            'busca_alternativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_buscar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.BuscarAyuda']", 'symmetrical': 'False'}),
            'ha_ayudado': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invita_actividad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_hace_nada': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_hace_problema': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'no_sabe': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'se_acerca': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'encuesta.aporta': {
            'Meta': {'object_name': 'Aporta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.asuntopublicovbg': {
            'Meta': {'object_name': 'AsuntoPublicoVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'resolverse_con': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ResolverVBG']", 'symmetrical': 'False'})
        },
        'encuesta.buscarayuda': {
            'Meta': {'object_name': 'BuscarAyuda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.calidadatencion': {
            'Meta': {'object_name': 'CalidadAtencion'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_porque': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'no_porque2': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'propuesta': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'propuesta2': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'si_tipo': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'si_tipo2': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'valor_servicio': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.causavbg': {
            'Meta': {'object_name': 'CausaVBG'},
            'causa': ('django.db.models.fields.IntegerField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.comoafecta': {
            'Meta': {'object_name': 'ComoAfecta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.composicionhogar': {
            'Meta': {'object_name': 'ComposicionHogar'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'cuantos_viven': ('django.db.models.fields.IntegerField', [], {}),
            'entre0y6': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entre18ymas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entre7y17': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hijos0y6': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hijos18ymas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hijos7y17': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tiene_hijos': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tiene_pareja': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'vive_con': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ViveCon']", 'symmetrical': 'False'})
        },
        'encuesta.comunicacionasertiva': {
            'Meta': {'object_name': 'ComunicacionAsertiva'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifico': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.SolucionConflicto']", 'symmetrical': 'False'}),
            'negociacion_exitosa': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.NegociacionExitosa']", 'symmetrical': 'False'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.conceptoviolencia': {
            'Meta': {'object_name': 'ConceptoViolencia'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sobre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'encuesta.conocimientoley': {
            'Meta': {'object_name': 'ConocimientoLey'},
            'adulto_dinero': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'adulto_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'existe_ley': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joven_case': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'joven_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'lider_religioso': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'maestro_castiga': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'maestro_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'mencione': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'padre_golpea': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'patron_acoso': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'})
        },
        'encuesta.contraparte': {
            'Meta': {'object_name': 'Contraparte'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'})
        },
        'encuesta.corresponsabilidad': {
            'Meta': {'object_name': 'Corresponsabilidad'},
            'acompanar': ('django.db.models.fields.IntegerField', [], {}),
            'arreglar_cama': ('django.db.models.fields.IntegerField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'cuidar_enfermos': ('django.db.models.fields.IntegerField', [], {}),
            'cuidar_ninos': ('django.db.models.fields.IntegerField', [], {}),
            'hacer_compras': ('django.db.models.fields.IntegerField', [], {}),
            'hacer_mandados': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ir_reuniones': ('django.db.models.fields.IntegerField', [], {}),
            'jalar_agua': ('django.db.models.fields.IntegerField', [], {}),
            'lavar': ('django.db.models.fields.IntegerField', [], {}),
            'lavar_trastes': ('django.db.models.fields.IntegerField', [], {}),
            'limpiar': ('django.db.models.fields.IntegerField', [], {}),
            'llevar_enfermos': ('django.db.models.fields.IntegerField', [], {}),
            'llevar_lena': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'pagar_servicios': ('django.db.models.fields.IntegerField', [], {}),
            'plancar': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.creencia': {
            'Meta': {'object_name': 'Creencia'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'creencia': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.decision': {
            'Meta': {'object_name': 'Decision'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.efectovbg': {
            'Meta': {'object_name': 'EfectoVBG'},
            'afecta_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'como_afecta': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ComoAfecta']", 'symmetrical': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.encuestador': {
            'Meta': {'object_name': 'Encuestador'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_completo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'})
        },
        'encuesta.espacio': {
            'Meta': {'object_name': 'Espacio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.expresionvbg': {
            'Meta': {'object_name': 'ExpresionVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maneras': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'encuesta.incidenciapolitica': {
            'Meta': {'object_name': 'IncidenciaPolitica'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'existen_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'satisfecha': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.informacionsocioeconomica': {
            'Meta': {'object_name': 'InformacionSocioEconomica'},
            'aportan': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Aporta']", 'symmetrical': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_trabaja': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.LugarDeTrabajo']", 'symmetrical': 'False'}),
            'estudia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hace_dinero': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_educativo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'trabaja_fuera': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.justificacionvbg': {
            'Meta': {'object_name': 'JustificacionVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'justificacion': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.lugardetrabajo': {
            'Meta': {'object_name': 'LugarDeTrabajo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.motivoparticipacion': {
            'Meta': {'object_name': 'MotivoParticipacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.mujer': {
            'Meta': {'object_name': 'Mujer'},
            'asiste_iglesia': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Contraparte']"}),
            'cual_iglesia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuestador']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar_origen': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'encuesta.negociacionexitosa': {
            'Meta': {'object_name': 'NegociacionExitosa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.participacionpublica': {
            'Meta': {'object_name': 'ParticipacionPublica'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'espacio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Espacio']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.MotivoParticipacion']", 'symmetrical': 'False'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.prevalenciavbg': {
            'Meta': {'object_name': 'PrevalenciaVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'frecuencia': ('django.db.models.fields.IntegerField', [], {}),
            'ha_vivido_vbg': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'que_tipo': ('django.db.models.fields.IntegerField', [], {}),
            'quien': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Quien']", 'symmetrical': 'False'})
        },
        'encuesta.quedebehacer': {
            'Meta': {'object_name': 'QueDebeHacer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.quien': {
            'Meta': {'object_name': 'Quien'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.recurso': {
            'Meta': {'object_name': 'Recurso'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'encuesta.resolvervbg': {
            'Meta': {'object_name': 'ResolverVBG'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.situacionvbg': {
            'Meta': {'object_name': 'SituacionVBG'},
            'conoce_hombres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'conoce_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.solucionconflicto': {
            'Meta': {'object_name': 'SolucionConflicto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.tomadecision': {
            'Meta': {'object_name': 'TomaDecision'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'decision': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Decision']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.vivecon': {
            'Meta': {'object_name': 'ViveCon'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'lugar.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['encuesta']
